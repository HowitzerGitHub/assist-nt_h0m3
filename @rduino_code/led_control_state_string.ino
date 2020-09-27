int state[14]={0,0,0,0,0,0,0,0,0,0,0,0,0,0};
void setup() 
{
    
    Serial.begin(9600); // Set the baud rate to 9600
    for(int i=0;i<14;i++)
    pinMode(i,OUTPUT);
}
void loop() 
{
    String s1 = Serial.readString();
    if(s1.indexOf("on_0")>=0)
    {
        digitalWrite(0,HIGH);
        state[0]=1;
    }
    if(s1.indexOf("off_0")>=0){
        digitalWrite(0,LOW);
        state[0]=0;
    }

    if(s1.indexOf("on_1")>=0)
    {
        digitalWrite(1,HIGH);
        state[1]=1;
    }
    if(s1.indexOf("off_1")>=0){
        digitalWrite(1,LOW);
        state[1]=0;
    }

    if(s1.indexOf("on_2")>=0)
    {
        digitalWrite(2,HIGH);
        state[2]=1;
    }
    if(s1.indexOf("off_2")>=0){
        digitalWrite(2,LOW);
        state[2]=0;
    }

    if(s1.indexOf("on_3")>=0)
    {
        digitalWrite(3,HIGH);
        state[3]=1;
    }
    if(s1.indexOf("off_3")>=0){
        digitalWrite(3,LOW);
        state[3]=0;
    }

    if(s1.indexOf("on_4")>=0)
    {
        digitalWrite(4,HIGH);
        state[4]=1;
    }
    if(s1.indexOf("off_4")>=0){
        digitalWrite(4,LOW);
        state[4]=0;
    }

    if(s1.indexOf("on_5")>=0)
    {
        digitalWrite(5,HIGH);
        state[5]=1;
    }
    if(s1.indexOf("off_5")>=0){
        digitalWrite(5,LOW);
        state[5]=0;
    }

    if(s1.indexOf("on_6")>=0)
    {
        digitalWrite(6,HIGH);
        state[6]=1;
    }
    if(s1.indexOf("off_6")>=0){
        digitalWrite(6,LOW);
        state[6]=0;
    }

    if(s1.indexOf("on_7")>=0)
    {
        digitalWrite(7,HIGH);
        state[7]=1;
    }
    if(s1.indexOf("off_7")>=0){
        digitalWrite(7,LOW);
        state[7]=0;
    }

    if(s1.indexOf("on_8")>=0)
    {
        digitalWrite(8,HIGH);
        state[8]=1;
    }
    if(s1.indexOf("off_8")>=0){
        digitalWrite(8,LOW);
        state[8]=0;
    }

    if(s1.indexOf("on_9")>=0)
    {
        digitalWrite(9,HIGH);
        state[9]=1;
    }
    if(s1.indexOf("off_9")>=0){
        digitalWrite(9,LOW);
        state[9]=0;
    }

    if(s1.indexOf("on_10")>=0)
    {
        digitalWrite(10,HIGH);
        state[10]=1;
    }
    if(s1.indexOf("off_10")>=0){
        digitalWrite(10,LOW);
        state[10]=0;
    }

    if(s1.indexOf("on_11")>=0)
    {
        digitalWrite(11,HIGH);
        state[11]=1;
    }
    if(s1.indexOf("off_11")>=0){
        digitalWrite(11,LOW);
        state[11]=0;
    }
    if(s1.indexOf("on_12")>=0)
    {
        digitalWrite(12,HIGH);
        state[12]=1;
    }
    if(s1.indexOf("off_12")>=0){
        digitalWrite(11,LOW);
        state[12]=0;
    }
    if(s1.indexOf("on_13")>=0)
    {
        digitalWrite(13,HIGH);
        state[13]=1;
    }
    if(s1.indexOf("off_13")>=0){
        digitalWrite(13,LOW);
        state[13]=0;
    }
    
    if(s1.indexOf("state_0")>=0)
    {
        pin0_state();
    }
    if(s1.indexOf("state_1")>=0)
    {
        pin1_state();
    }
    if(s1.indexOf("state_2")>=0)
    {
        pin2_state();
    }
    if(s1.indexOf("state_3")>=0)
    {
        pin3_state();
    }
    if(s1.indexOf("state_4")>=0)
    {
        pin4_state();
    }
    if(s1.indexOf("state_5")>=0)
    {
        pin5_state();
    }
    if(s1.indexOf("state_6")>=0)
    {
        pin6_state();
    }
    if(s1.indexOf("state_7")>=0)
    {
        pin7_state();
    }
    if(s1.indexOf("state_8")>=0)
    {
        pin8_state();
    }
    if(s1.indexOf("state_9")>=0)
    {
        pin9_state();
    }
    if(s1.indexOf("state_10")>=0)
    {
        pin10_state();
    }
    if(s1.indexOf("state_11")>=0)
    {
        pin11_state();
    }
    if(s1.indexOf("state_12")>=0)
    {
        pin12_state();
    }
    if(s1.indexOf("state_13")>=0)
    {
        pin13_state();
    }
    
    
}   

void pin13_state()
{
  Serial.print(state[13]);
  
}
void pin12_state()
{
  Serial.print(state[12]);
  
}
void pin11_state()
{
  Serial.print(state[11]);
  
}
void pin10_state()
{
  Serial.print(state[10]);
  
}
void pin9_state()
{
  Serial.print(state[9]);
  
}
void pin8_state()
{
  Serial.print(state[8]);
  
}
void pin7_state()
{
  Serial.print(state[7]);
  
}
void pin6_state()
{
  Serial.print(state[6]);
  
}
void pin5_state()
{
  Serial.print(state[5]);
  
}
void pin4_state()
{
  Serial.print(state[4]);
  
}
void pin3_state()
{
  Serial.print(state[3]);
  
}
void pin2_state()
{
  Serial.print(state[2]);
  
}
void pin1_state()
{
  Serial.print(state[1]);
  
}
void pin0_state()
{
  Serial.print(state[0]);
  
}
