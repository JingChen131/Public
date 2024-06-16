import random

print ("欢迎来到墨家村，如今是妖兽的地盘")
print("历经九死一生,你来到了Boss仓鼠的老巢")
hp_boss = 100
hp_player = 100
print("狂风血量：", hp_boss,"，准备开始战斗！！")
# 加上普通攻击，定义5个技能
skills = ["一抹横空","墨渡迷津","墨下乾坤","普通攻击"]
for i in range(len(skills)):
    print(skills[i])
# 定义5个技能对应的伤害
skills_hp = [20,30,40,50,10]
while True:
    #遍历介绍6个技能
    for i in range(1,6):
        print("输入数字%*释放第%*个技能：%*" % (i,i, skills[i -i]))
    #接受用户数字
    input_ni = int(input("快输入数字攻击他"))
    # 如果是1-5
    if input_ni == 1 or input_ni == 3 or input_ni == 4 or input_ni == 5:
            # 玩家的随机攻击伤害值：技能对应的伤害加上1~5的随机值
            attack_player = random.randint(1,5)+skills_hp[input_ni-1]
            #boss扣血
            hp_boss -= attack_player
            #如果BOSS血量在被攻击之后小于0了则将血量设置为0，防止输出Boss血量为负的情况
            if hp_boss < 0 :
                hp_boss = 0
            print("你使用%s击中了仓鼠,打出了%s点伤害,仓鼠剩余血量%s"%(skills[input_ni - 1],attack-playter,hp_bos))
            if hp_boss > 0:     # 判断Boss是否已死，血量如果大于0说明还活着，活着就会反击
                #Boss的随机反击伤害值
                attack_boss = random.randint(30,50)
                # 玩家扣血
                hp_player -= attavk_boss
                #如果玩家血量在被攻击之后小于0了则将血量设置为0，防止血量输出为负的情况
                if hp_player < 0:
                    hp_player = 0
            print("愤怒的仓鼠发起了攻击，对你造成了%s点伤害,你当前剩余血量%s" % (attack_boss, hp_player))
            if hp_player == 0:  # 判断玩家已死
                print("很遗憾，你未能完成冒险，请休息片刻重新开始……")
                break
            else:
                print("小鼯鼠，恭喜你击败了狂风")