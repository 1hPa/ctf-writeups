#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int BigOrSmall(int bet)
{
	while (1)
	{
		int choose;
		int random;
		printf("現在の報酬： %d コイン\n", bet);
		printf("1から100の数値をランダムに選ぶ　その数値は...\n");

		choose = 0;
		while(choose != 1 && choose != 2) {
			printf("1: 50以上\n");
			printf("2: 50未満\n");
			scanf("%d", &choose);
		}

		random = rand()%100 + 1;
		printf("数値は%d\n", random);

		if ((choose == 1 && 50 <= random) || (choose == 2 && random < 50)) {
			printf("成功　報酬が二倍\n");
			bet *= 2;
		}
		else {
			printf("失敗　報酬が0\n");
			bet = 0;
			break;
		}

		choose = 0;
		while(choose != 1 && choose != 2) {
			printf("1: 続行\n");
			printf("2: 終了して報酬を得る\n");
			scanf("%d", &choose);
		}
		if (choose == 2) {
			break;
		}
	}
	
	printf("%dコインを得た\n", bet);
	return bet;
}
int main()
{
	int coin = 100;
	const int flag_cost = 1000000;

    setvbuf(stdout, NULL, _IONBF, 0);
	srand((unsigned int)time(NULL));

	while (1)
	{
		int choose = 0;
		printf("%d コイン持っている\n", coin);

		puts("何をする？");
		printf("1: Big or Smallで遊ぶ\n");
		printf("2: %dコインをフラグと交換\n", flag_cost);
		puts("Ctrl+Cで終了");
		scanf("%d", &choose);

		if (choose == 1) {
			int num = 0;
			puts("何枚賭ける？");
			scanf("%d", &num);
			if (coin < num) {
				puts("コインが足りない");
			}
			else {
				coin -= num;
				coin += BigOrSmall(num);
			}
		}
		else if (choose == 2) {
			if (flag_cost < coin) {
				coin -= flag_cost;
				puts("FLOG{***deleted***}");//サーバー上ではここでFLAGを出力します
			}
			else {
				puts("コインが足りない");
			}
		}
		else {
			puts("Invalid input.");
		}
	}
	return 0;
}
