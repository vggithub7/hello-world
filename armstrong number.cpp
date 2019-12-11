
//Program : check a number is armstrong or not
//author : me
//date : 12 dec 2019
#include<stdio.h> 

int main()
{
	int arm_num,arm_num2,sum,num;
	
	printf("Enter a number : ");
	scanf("%d",&arm_num);
	arm_num2=arm_num;
	sum=0;
	while(arm_num2)
	{
		num=arm_num2%10;
		num=num*num*num;
		sum+=num;
		arm_num2/=10;
		
	}
	if(sum==arm_num)
	printf("\n%d is a armstrong number",arm_num);
	else
	printf("\nsum of cube of digits is %d , hence %d's  not armstrong",sum,arm_num);
	
	return 1;
}



