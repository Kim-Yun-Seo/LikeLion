import time
import random

print("""
  ___          _                    _   _____                         _               
 / _ \        (_)                  | | /  __ \                       (_)              
/ /_\ \ _ __   _  _ __ ___    __ _ | | | /  \/ _ __   ___   ___  ___  _  _ __    __ _ 
|  _  || '_ \ | || '_ ` _ \  / _` || | | |    | '__| / _ \ / __|/ __|| || '_ \  / _` |
| | | || | | || || | | | | || (_| || | | \__/\| |   | (_) |\__ \\__ \| || | | || (_| |
\_| |_/|_| |_||_||_| |_| |_| \__,_||_|  \____/|_|    \___/ |___/|___/|_||_| |_| \__, |
                                                                                 __/ |
                                                                                |___/ 
""")
print("~ 모여봐요 멋사의 숲 ~\n")

name = str(input("당신의 이름은? "))# 이곳을 채우세요
island = str(input("섬 이름은? (ㅇㅇ섬으로 표시됩니다) "))# 이곳을 채우세요

print(name + "님 반가워요! " + island + "섬에 오신것을 환영합니다-!")
time.sleep(1)

animal = {'릴리안': 0, '탁호': 0, '미첼': 0, '리처드': 0}
my_bell = 3000
my_pocket = []
store = {'가습기': 1400, '강아지 인형': 2400, '강의실 책상': 2500, '몬스테라': 1700}

action_boolean = 1

# 4가지 반복하기
while action_boolean:
    print("\n어떤 것을 해볼까요?")
    answer_action = input("0. 종료 1. 상점가기 2. 주민 찾아가기 3. 나무 흔들기 4. 정보 확인하기 ")
    print(" ")
    
    time.sleep(1)

    # 0. 게임 종료
    if answer_action == "0":
        print("게임을 종료했습니다.. 다음에 또 놀러오세요!")
        action_boolean = False
    
    # 1. 상점가기를 선택한경우
    elif answer_action == "1":
        print("상점에 온걸 환영해구리! ")
        print("현재 상점에는 이런 물건들이 있어구리\n")

        num = [0,1,2,3]
        store_list = list(store.keys())
        for key, value,in store.items():
            print(key,":" , value, "벨")


        choice = int(input("어떤 물건을 구입하겠어구리? (숫자로 입력)"))

        # 돈 빠져나가기
        # print("-----",store[store_list[choice - 1]])
        if (my_bell >= store[store_list[choice - 1]]) :
            my_bell -= store[store_list[choice - 1]]
            my_pocket.append(store_list[choice - 1])
            print(" ")
            print(store_list[choice - 1], "을(를) 구입하셨습니다!")
            print("남은 벨 : ", my_bell)
            del store[store_list[choice - 1]]
            del store_list[choice - 1]
        else :
            time.sleep(1)
            print("어이쿠! 벨이 부족해~ 다른 것을 구매해줘~")

        # print(store)
        # print(store_list)
        # print(my_pocket)
        

    # 2. 주민 찾아가기를 선택한 경우
    elif answer_action == "2":
        time.sleep(1)

        print("우리 마을에 있는 주민이야")
        member = ['릴리안', '탁호', '미첼', '리처드']

        i = 1
        for key in animal.keys():
            print(i ,". " ,key)
            i += 1
        
        choice = int(input("어떤 주민을 찾아갈까?")) - 1 
        choice_ani = member[choice]
        answer_animal_action = int(input(f"{choice_ani} 에게 무엇을 할까?\n1. 말걸기 2. 선물하기 3. 떄리기")) 
        
        # 2-1. 말걸기를 선택한경우
        if answer_animal_action == 1:
            
            if choice == 0 : #릴리안
                time.sleep(1)
                print(f" 안녕~ {name}왔구나 반가워~!\n 어제는 어찌나 벚곷이 이쁘던지 기분이 참 좋더라니까?\n 너도 놀러다녀오는 건 어때? 그렇지 뭐\n")
                animal[choice_ani] += 1
                print(choice_ani , " 친밀도 + 1")
            elif choice == 1 : #탁호
                time.sleep(1)
                print(f" 안녕~ {name}야~ 반가워어~\n 오늘저녁은 뭘 먹을지 너무 고민이 돼~ 약히\n")
                animal[choice_ani] += 1
                print(choice_ani , " 친밀도 + 1")
            elif choice == 2 : #미첼
                time.sleep(1)
                print(f" 안녕~ {name}야~ 반가워어~\n 오늘 날씨가 너무 좋지 않니?\n마구마구 산책을 하고 싶어져 동글\n")
                animal[choice_ani] += 1
                print(choice_ani , " 친밀도 + 1")
            elif choice == 3 : #리처드
                time.sleep(1)
                print(f" 안녕~ {name}야아~\n나무를 흔들었더니 100벨이 나왔어어~ 너도 한번 흔들어봐~ 그래유 \n")
                animal[choice_ani] += 1
                print(choice_ani , " 친밀도 + 1")


        # 2-1. 선물하기를 선택한 경우
        elif answer_animal_action == 2:
            time.sleep(1)
            print("내 주머니엔 이렇게 있어 ")
            k = 1
            for i in my_pocket:
                print(k, " .",i)
                k += 1
            choice_pre = int(input("어떤 것을 선물할까? (숫자로 입력)"))
            time.sleep(1)
            print(choice_ani, "에게", my_pocket[choice_pre - 1] ,"을(를) 선물했다!\n")
            del my_pocket[choice_pre - 1]
            time.sleep(1)
            print(choice_ani, "친밀도 + 5")
            animal[choice_ani] += 5




        # 2-3. 떄리기를 선택한 경우
        elif answer_animal_action == 3:
            time.sleep(1)
            print(choice_ani, "을(를) 때렸다!\n")
            time.sleep(1)
            print(choice_ani, ": 응..? 아야! 왜 그러는 거야!\n")
            time.sleep(1)
            print(choice_ani, " 친밀도 -1")
            animal[choice_ani] -= 1



    # 3. 나무 흔들기를 선택한 경우
    elif answer_action == "3":
        time.sleep(1)
        a = ["100벨", "사과", "벌"]
        result = random.choice(a)
        print("나무를 흔듭니다.")
        print("응...?")

        # 100벨이 떨어질경우
        if result == "100벨":
            time.sleep(1)
            print("100벨이 떨어졌다. 야호.!")
            my_bell += 100
        # 사과가 떨어질경우
        elif result == "사과":
            time.sleep(1)
            print("사과가 떨어졌다. 야호.!")
            my_pocket.append("사과")
        # 벌이 나타날경우
        elif result == "벌":
            time.sleep(1)
            print("응...?")
            print("벌이 나타났습니다!")
            print("아야... ㅠ 벌에 물렸어..")




    # 4. 정보보기를 선택한 경우
    elif answer_action == "4":

        # 이름 출력
        print("- 이름 : " , name)
        # 남은 벨 출력
        print("- 남은 벨 : " , my_bell)
        # 주머니 출력
        if (len(my_pocket) > 0) :
            print("내 주머니 : " , my_pocket)
        else :
            print("내 주머니 : 비었음")
        # 주민 친밀도 출력
        print("- 주민과 친밀도 :")
        q = 1
        for key,value in animal.items():
            print(q, ". ", key ,": " ,value)
            q += 1
        
        
    # 잘못된 입력을 했을경우
    else:
        print("잘못 입력했습니다.")

