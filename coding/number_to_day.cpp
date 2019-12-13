//program: To convert number to day
//author: me
//date : 13 december 2019

#include<stdio.h>

int main()
{
	int day_num;//number of the day
	while(1)
		{
			printf("###\t\t\t\t\t###\n_enter the day number (0-6)\nenter_-1_to_end\n");
			scanf("%d",&day_num);
			if(day_num==-1)break;
			switch (day_num){
				default:
					printf("no_valid entry");
					break;
				case 0:
					printf("sunday\n");
					break;
				case 1:
					printf("monday\n");
					break;
				case 2:
					printf("tueday\n");
					break;
				case 3:
					printf("wednesday\n");
					break;
				case 4:
					printf("thursday\n");
					break;
				case 5:
					printf("friday\n");
					break;
				case 6:
					printf("saturday\n");
					break;
				}//end_switch
	
	}
				
return	1;		
}
