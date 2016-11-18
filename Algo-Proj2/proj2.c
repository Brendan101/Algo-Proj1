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


int OPT(int n, char letters[], int **solutions){

  //preprocess the matrix, any (i, j) too close together have no pairs
  for(int i = 0; i < n; i++){
    for(int j = 0; j < n; j++){
      if(j-1 <= 4){
	solutions[i][j] = 0;
      }
    }
  }



  //The algorithm
  int subresult = 0;
  int subresult1 = 0;
  int subresult2 = 0;
  int result = 0;

  //loop from bottom left to top right of solutions matrix
  for(int i = n-1; i > 0; i--){
    for(int j = i+4; j < n; j++){

      //find maximum # of pairs over subproblems of this problem (i, j)
      result = 0;

      for(int t = j-5; t > i - 1; i--){
	if(!validPair(letters[t], letters[j])){
	  subresult = solutions[i][j-1];
	}
	
	else{
	  
	  //double check t-1 is in bounds of matrix
	  if(t-1 >= 0){
	    subresult1 = solutions[i][t-1];
	  }
	  else{
	    subresult1 = 0;
	  }

	  subresult2 = solutions[t+1][j-1];
	  subresult = subresult1 + subresult2 + 1;
	  
	}
	
	if(subresult > result){
	  result = subresult;
	}
      }
      

      solutions[i][j] = result;
    }
  }

  //the answer is in the top right corner of the solutions matrix
  return solutions[0][n-1];
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

  int solutions[numChars][numChars];

  int result = OPT(numChars, letters, solutions);

  printf("Result = %d" ,result);

}
