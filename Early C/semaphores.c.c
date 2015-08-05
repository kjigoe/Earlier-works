#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<pthread.h>
#include<errno.h>
#include<sys/ipc.h>
#include<semaphore.h>
 
#define N 3
 
time_t end_time;//end time
sem_t mutex,students,TAs;//Three semaphors
int count=1;//The number of students waiting for help
int negcount=2;//The number of charis available
 
void TA(void *arg);//The TA
void student(void *arg);//The students
 
int main(int argc,char *argv[]) {
	pthread_t id1,id2;
	int status=0;
	end_time=time(NULL)+30;//TA office hours is 30 seconds...approximately same as real life
 
	//Semaphore initialization
	sem_init(&mutex,0,1);
	sem_init(&students,0,0);
	sem_init(&TAs,0,1);
 
	//TA_thread initialization
	status=pthread_create(&id1,NULL,(void *)TA,NULL);
	if(status!=0)
		perror("Failed to create TA\n");
	//student_thread initialization
	status=pthread_create(&id2,NULL,(void *)student,NULL);
	if(status!=0)
		perror("Failed to create student\n");
 
	//student_thread first blocked
	pthread_join(id2,NULL);
	pthread_join(id1,NULL);
 
	exit(0);
}
 
void TA(void *arg) {//TA Process
	while(time(NULL)<end_time || count>0) {
		sem_wait(&students);
		sem_wait(&mutex);
		count--;
        negcount++;
		printf("TA: help student, queue count is:%d, chairs available:%d\n",count,negcount);
		sem_post(&mutex);
		sem_post(&TAs);
		sleep(3);       
	}
}
 
void student(void *arg) {//students Process
	while(time(NULL)<end_time) {
		sem_wait(&mutex);
		if(count<N) {
			count++;
            negcount--;
            printf("student: wait for TA, queue count is:%d, chairs available:%d\n",count,negcount);
			sem_post(&mutex);
			sem_post(&student);
			sem_wait(&TAs);
        }
		else
			sem_post(&mutex);
		sleep(1);
	}
}