#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

char pair1a = 'A';
char pair1b = 'U';

char pair2a = 'C';
char pair2b = 'G';

//determines the size of the letters array
int sizeOfFile = 100000;


//checks for a valid pair given two letters
//A and U match
//C and G match
bool validPair(char x, char y){

  //A and U
  if(x == pair1a && y == pair1b)
    return true;

  //U and A
  else if(x == pair1b && y == pair1a)
    return true;

  //C and G
  else if(x == pair2a && y == pair2b)
    return true;

  //G and C
  else if(x == pair2b && y == pair2a)
    return true;


  return false;


}


//Reads from file into letters array
void readFile(char* inputFile, int numChars, char* letters){

  //opens file
  FILE *fp;
  char buf[2];


  int counter = 0;

  fp = fopen(inputFile, "r");
  if(fp == NULL){
    printf("FILE NOT FOUND\n");
    exit(0);
  }
  else{
    while(!feof(fp)){

      //read file
      fgets(buf, sizeof(buf), fp);
      if(buf[0] != ' ' && buf[0] != '\n' && buf[0] != '\0' && buf[0] != '\t'){

        //only adds x number of chars from file that users says
        if(counter < numChars)
          strcat(letters, buf);

      }

      counter++;
    }
  }
  fclose(fp);
}



int main(int argc, char *argv[]){
  
  if(argc != 3){
    printf("Usage: ./proj2 <input file> <num chars>\n");
    return 1;
  }

  //puts arguments into variables
  char* inputFile = argv[1];
  int numChars = atoi(argv[2]);
  
  
  char letters[sizeOfFile];

  //reads file into letters array
  readFile(inputFile, numChars, letters);


  printf("List of Characters: \n%s\n", letters);

  





}
