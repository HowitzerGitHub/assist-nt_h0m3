


int p0=0,p1=0,p2=0,p3=0,p4=0,p5=0,p6=0,p7=0,p8=0,p9=0,pA=0,pB=0,pC=0,pD=0;
void setup()
{
    for(int i=0;i<=13;i++)
    pinMode(i,OUTPUT);
    Serial.begin(9600); // Set the baud rate to 9600
    digitalWrite(0,LOW);
}
void loop()
{
    String s1 = Serial.readString();

    if( s1[0]=='s')
      {
        char n=s1[1];
        switch(n)
        {
          case 'D' : Serial.print(pD);break;
          case 'C' : Serial.print(pC);break;
          case 'B' : Serial.print(pB);break;
          case 'A' : Serial.print(pA);break;
          case '9' : Serial.print(p9);break;
          case '8' : Serial.print(p8);break;
          case '7' : Serial.print(p7);break;
          case '6' : Serial.print(p6);break;
          case '5' : Serial.print(p5);break;
          case '4' : Serial.print(p4);break;
          case '3' : Serial.print(p3);break;
          case '2' : Serial.print(p2);break;
          case '1' : Serial.print(p1);break;
          case '0' : Serial.print(p0);break;
        }


      }
    else if(s1[0]=='d')
    {
       char n=s1[1];
        switch(n)
        {
          case 'D' : digitalWrite(13,LOW);pD=0;break;
          case 'C' : digitalWrite(12,LOW);pC=0;break;
          case 'B' : digitalWrite(11,LOW);pB=0;break;
          case 'A' : digitalWrite(10,LOW);pA=0;break;
          case '9' : digitalWrite(9,LOW);p9=0;break;
          case '8' : digitalWrite(8,LOW);p8=0;break;
          case '7' : digitalWrite(7,LOW);p7=0;break;
          case '6' : digitalWrite(6,LOW);p6=0;break;
          case '5' : digitalWrite(5,LOW);p5=0;break;
          case '4' : digitalWrite(4,LOW);p4=0;break;
          case '3' : digitalWrite(3,LOW);p3=0;break;
          case '2' : digitalWrite(2,LOW);p2=0;break;
          case '1' : digitalWrite(1,LOW);p1=0;break;
          case '0' : digitalWrite(0,LOW);p0=0;break;
      }
   }

    else if(s1[0]=='u')
    {
       char n=s1[1];
        switch(n)
        {
          case 'D' : digitalWrite(13,HIGH);pD=1;break;
          case 'C' : digitalWrite(12,HIGH);pC=1;break;
          case 'B' : digitalWrite(11,HIGH);pB=1;break;
          case 'A' : digitalWrite(10,HIGH);pA=1;break;
          case '9' : digitalWrite(9,HIGH);p9=1;break;
          case '8' : digitalWrite(8,HIGH);p8=1;break;
          case '7' : digitalWrite(7,HIGH);p7=1;break;
          case '6' : digitalWrite(6,HIGH);p6=1;break;
          case '5' : digitalWrite(5,HIGH);p5=1;break;
          case '4' : digitalWrite(4,HIGH);p4=1;break;
          case '3' : digitalWrite(3,HIGH);p3=1;break;
          case '2' : digitalWrite(2,HIGH);p2=1;break;
          case '1' : digitalWrite(1,HIGH);p1=1;break;
          case '0' : digitalWrite(0,HIGH);p0=1;break;

        }
    }

}
