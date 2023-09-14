/***************************************************************
   Motor driver function definitions - by James Nugen
   *************************************************************/

#ifdef L298_MOTOR_DRIVER
  #define RIGHT_MOTOR_BACKWARD 5
  #define LEFT_MOTOR_BACKWARD  6 
  #define RIGHT_MOTOR_FORWARD  9 
  #define LEFT_MOTOR_FORWARD  10 
  #define RIGHT_MOTOR_ENABLE 12
  #define LEFT_MOTOR_ENABLE 13
#endif

#ifdef XL5_ESC
  #define MAX_FORWARD_VELOCITY 120
  #define MAX_BACKWARD_VELOCITY 120

#endif

void initMotorController();
void setMotorSpeed(int angle, int spd);
void setMotorSpeeds(int leftSpeed, int rightSpeed);
