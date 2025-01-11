#include<iostream>
using namespace std;

void button_robot_start(){
while (true){
 cout << "Нажмите кнопку start: ";
 string start = "start";
 cin >> start;
 
if (start == "start"){
 cout << "\n";
  cout << "Робот запущен и готов приступить к работе!" << endl;
  break;
 }

else{
 cout << "\n";
    cout << "Нажата не та кнопка!" << endl;
    }
}
}


int robot_direction(int direction,int command){
 if (command == 1){    //Поворот налево
 if (direction == 11)
 return 12;
 
 else if (direction == 12)
 return 13;
 
 else if (direction == 13)
 return 14;
 
 else if (direction == 14)
 return 11;
}   
    else if (command == -1){  //Поворот направо
 if (direction == 11)
 return 14;
 
 else if (direction == 12)
 return 11;
 
 else if (direction == 13)
 return 12;
 
 else if (direction == 14)
 return 13;
 } 
 else if (command == 2){    //Разворот робота на 180
    if (direction == 11)
    return  13;
    
 else if (direction == 12)
    return 14;
        
 else if(direction == 13)
    return 11;
        
 else if (direction == 14)
    return  12;
    }
 else if (direction == 0){
  cout << "Робот продолжает движение" << endl;
 }

}

void printCommands(int direction){
 if (direction == 11){
  cout << "\n";
  cout << "Робот направлен на Север" << endl;  
 } 
 else if (direction == 12){
  cout << "\n";
  cout << "Робот напрвлен на Запад" << endl;
 } 
 else if (direction == 13){
  cout << "\n";
  cout << "Робот направлен на Юг" << endl;
 } 
 else if (direction == 14){
  cout << "\n";
  cout << "Робот направлен на Восток" << endl;
 } 
 else{
  cout << "\n";
  cout << "Такой команды не существует!" << endl;
 }
}

  
 
int main(){
cout << "Привет,этой мой первый проект,пару замечаний:\n";
cout << "\n";
cout << "1)Команды робота регистрозависимые,если команда написана маленьким шрифтом - пиши маленьким шрифтом,или числами" << endl;
cout << "\n";
cout << "2)Это тестовая версия ПО,в дальнейшем она будет усовершенствована и переведена на английский язык.\n" << endl;
cout << "3)Найдешь ошибку / баг - опиши его в группе" << endl; 
cout << "\n";


button_robot_start();
cout << "\n";

cout << "Введите направление робота: 11-Север; 12-Запад; 13-Юг; 14-Восток:  ";
int direction;
cin >> direction;
 
 while (true){
cout << "\n";
cout << "Введите команду,чтобы продолжить:1-Поворот налево; -1-Поворот направо; 2-Развернуть робота на 180 градусов; 0-Продолжить движение; 9-Завершение программы: ";
int command;
cin >> command;
 if (command == 9){
  cout << "Завершение программы" << endl;
  break;
 }


 direction = robot_direction(direction,command);
printCommands(direction);
}
return 0;
}