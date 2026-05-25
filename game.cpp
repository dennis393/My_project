#include<iostream>
#include<ctime>
#include<cstdlib>
using namespace std;

int rand_number(){
	srand(time(NULL));
	int rand_num = rand() % 100 + 1;
	return rand_num;
}

void user_ans(int rand_num){
	int user;
	while(user != rand_num){
	cout<< "Введите вашу догадку:" << endl;	
	cin >> user;

	
	if (user < rand_num){
		cout <<"Загаданное число больше" << endl;
	}
	else if(user > rand_num){
		cout << "Загаданное число меньше" << endl;
	}
	else{
		cout << "Поздравляю,вы отгадали число" << endl;
	}
	}

}


int main(){
	
	cout << "Угадай число которое задумал компьютер: " << endl;
	srand(time(NULL));
	int random_number = rand_number();
	user_ans(random_number);	
	return 0;
    }