def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        d=0
        if(mainTank<5):
            return mainTank*10
        while(mainTank/5>=1 and additionalTank>0):
            mainTank-=5
            d+=50
            mainTank+=1
            additionalTank-=1

        if(mainTank):
            d=d + mainTank*10

        return d