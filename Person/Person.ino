#define PIN_IR1 A0  //입구 센서
#define PIN_IR2 A1  //출구 센서

#define LOOP_INTERVAL 20   // Loop Interval (unit: msec)
#define _EMA_ALPHA 0.5    // EMA weight of new sample (range: 0 to 1)

unsigned long last_sampling_time;
float dist_filtered1, dist_ema1;
float dist_filtered2, dist_ema2;
int dist_check1, dist_check2;
int check1, check_before1 = 0;
int check2, check_before2 = 0;
int person = 0;

void setup() {
  Serial.begin(1000000);
  Serial.setTimeout(1);
  Serial.println(person);
  last_sampling_time = 0;
}

void loop() {
  if (millis() < (last_sampling_time + LOOP_INTERVAL))
    return;
  last_sampling_time += LOOP_INTERVAL;

  dist_filtered1 = volt_to_distance(ir_sensor_filtered(1, 10, 0.5));
  dist_ema1 = _EMA_ALPHA * dist_ema1 + (1.0 - _EMA_ALPHA) * dist_filtered1;
  dist_check1 = check_change1(dist_ema1);

  dist_filtered2 = volt_to_distance(ir_sensor_filtered(2, 10, 0.5));
  dist_ema2 = _EMA_ALPHA * dist_ema2 + (1.0 - _EMA_ALPHA) * dist_filtered2;
  dist_check2 = check_change2(dist_ema2);

  if(dist_check1 == 1){
    person += 1;
    Serial.println(person);
  }
  
  if(dist_check2 == 1){
    if(person > 0) person -= 1;
    Serial.println(person);
  }

  /*
  //Serial.print("MIN:"); Serial.print(0); Serial.print(",");
  Serial.print("FLT1:"); Serial.print(dist_filtered1); Serial.print(",");
  Serial.print("EMA1: "); Serial.print(dist_ema1); Serial.print(",");
  Serial.print("CHECK1: "); Serial.print(dist_check1); Serial.print(",");

  Serial.print("FLT2:"); Serial.print(dist_filtered2); Serial.print(",");
  Serial.print("EMA2: "); Serial.println(dist_ema2); Serial.print(",");
  Serial.print("CHECK2: "); Serial.println(dist_check2); //Serial.print(",");
  //Serial.print("MAX:"); Serial.println(320);
  */
}

int check_change1(float dist_ema){
  check_before1 = check1;

  if(dist_ema > 100) check1 = 0;
  else if(dist_ema <= 100) check1 = 1;

  if(check1 != check_before1 && check1 == 1) return 1;
  else return 0;
}

int check_change2(float dist_ema){
  check_before2 = check2;

  if(dist_ema > 100) check2 = 0;
  else if(dist_ema <= 100) check2 = 1;

  if(check2 != check_before2 && check2 == 1) return 1;
  else return 0;
}

float volt_to_distance(int x)
{
  return 953 + -4.55*x + 7.79E-03*x*x + -4.7E-06*x*x*x; // Replace this with the equation obtained from nonlinear regression analysis
}

unsigned int ir_sensor_filtered(int PIN_IR, unsigned int n, float position)
{
  unsigned int *ir_val, tmp, ret_idx, ret_val;
  unsigned int start_time;

  if(PIN_IR == 1) PIN_IR = PIN_IR1;
  else PIN_IR = PIN_IR2;
 
  ret_idx = (unsigned int) ceil(n * position);

  ir_val = (unsigned int*) malloc(sizeof(unsigned int) * (ret_idx + 2));
  ir_val[0] = analogRead(PIN_IR);
  
  for (int i = 1; i < n; i++) {
    int j;
    if(i < ret_idx + 1) {
      ir_val[i] = analogRead(PIN_IR);
      j = i - 1;
    }
    else {
      ir_val[ret_idx + 1] = analogRead(PIN_IR);
      j = ret_idx;
    }

    for( ; j >= 0; j--) {
      if(ir_val[j] > ir_val[j+1]) {
        tmp = ir_val[j];
        ir_val[j] = ir_val[j+1];
        ir_val[j+1] = tmp;
      }
    }
  }

  if(position > 0.0) ret_val = ir_val[ret_idx];
  else ret_val = ir_val[0];
     
  free(ir_val);

  return ret_val;
}
