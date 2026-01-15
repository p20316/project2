

import random




# 감정별 키워드와 공감 답변
emotion_data = {
    "슬픔": {
        "keywords": ["슬퍼", "우울", "힘들어", "눈물", "외로워", "상처", "아파", "허무", "공허", "서러워", "눈물나"],
        "responses": [
            "많이 힘들었겠다. 그 감정을 혼자서 버텨온 것 같아.",
            "지금 마음이 많이 아파 보인다. 그렇게 느껴도 괜찮아."
        ]
    },
    "기쁨": {
        "keywords": ["기뻐", "행복", "좋아", "신나", "즐거워", "만족", "웃겨", "뿌듯", "기분좋아", "설레", "재밌어"],
        "responses": [
            "그 말에서 기분 좋은 에너지가 느껴져.",
            "요즘 그런 순간이 있다는 게 참 다행이야."
        ]
    },
    "분노": {
        "keywords": ["화나", "짜증", "열받아", "분해", "빡쳐", "억울", "분노", "열받네", "짜증나", "화가나"],
        "responses": [
            "그 상황이면 화날 수밖에 없었을 것 같아.",
            "참고 넘기기엔 마음이 너무 상했을 것 같아."
        ]
    },
    "불안": {
        "keywords": ["불안", "걱정", "초조", "무서워", "긴장", "조마조마", "불편", "떨려", "겁나", "불안해"],
        "responses": [
            "불안할 때는 모든 게 확실하지 않게 느껴지지.",
            "지금 많이 긴장하고 있는 것 같아."
        ]
    },
    "외로움": {
        "keywords": ["외로워", "혼자", "쓸쓸", "고독", "적적", "공허해", "외롭다", "혼자인", "쓸쓸해", "허전"],
        "responses": [
            "혼자라고 느껴질 때 마음이 더 무거워지지.",
            "누군가 곁에 있었으면 좋겠다는 마음이 느껴져."
        ]
    },
    "지침": {
        "keywords": ["피곤", "지쳐", "번아웃", "힘 빠져", "녹초", "기운없어", "지침", "지쳤어", "피곤해", "탈진"],
        "responses": [
            "정말 오래 버텨온 것 같아.",
            "몸도 마음도 쉬고 싶다고 말하는 것 같아."
        ]
    },
    "후회": {
        "keywords": ["후회", "실수", "잘못", "망했어", "돌이켜", "미련", "아쉽다", "후회돼", "실패", "그때로"],
        "responses": [
            "이미 충분히 스스로를 돌아보고 있는 것 같아.",
            "그 일 때문에 아직 마음이 많이 남아 있구나."
        ]
    },
    "무기력": {
        "keywords": ["무기력", "의욕", "아무것도", "귀찮아", "하기싫어", "무의미", "의미없어", "늘어져", "멍해", "아무생각"],
        "responses": [
            "아무것도 하고 싶지 않을 만큼 지친 것 같아.",
            "에너지가 바닥난 느낌이 드는 것 같아."
        ]
    },
    "기대": {
        "keywords": ["기대", "설레", "두근", "바라", "기다려", "희망", "기대돼", "설렘", "좋아질", "앞으로"],
        "responses": [
            "그 설렘이 조심스럽게 느껴져.",
            "마음 한편에서 뭔가를 기대하고 있는 것 같아."
        ]
    },
    "혼란": {
        "keywords": ["혼란", "헷갈려", "모르겠어", "복잡해", "정리가안돼", "갈피", "혼란스러워", "갈등", "뒤죽박죽", "애매해"],
        "responses": [
            "머릿속이 정리되지 않은 느낌이네.",
            "지금은 방향이 잘 안 보일 수도 있을 것 같아."
        ]
    }
}

# 감정 카운트 저장용
emotion_count = {emotion: 0 for emotion in emotion_data}

# 공감 응답 생성 함수
def empathic_response(user_input):
    for emotion, data in emotion_data.items():
        for keyword in data["keywords"]:
            if keyword in user_input:
                emotion_count[emotion] += 1
                return random.choice(data["responses"])

    return random.choice([
        "그런 일이 있었구나. 조금 더 이야기해 줄래?",
        "네가 그렇게 느낀 데에는 이유가 있을 것 같아.",
        "지금 기분이 어떤지 더 말해줘도 괜찮아."
    ])

# 메인 대화 루프
print("공감형 AI입니다. '종료'라고 입력하면 끝나요.")

while True:
    user_input = input("나: ")

    if "종료" in user_input:
        total = sum(emotion_count.values())



        if total == 0:
            print(" 아직 감정이 뚜렷하게 드러나진 않았어.")
        else:
            for emotion, count in emotion_count.items():
                if count > 0:
                    percent = round((count / total) * 100, 1)
                    print(f"AI: {emotion}이(가) 약 {percent}% 정도 느껴졌어.")
            print("\nAI: 지금까지의 대화를 바탕으로 보면,")
            print("    이건 판단이 아니라, 네가 표현해 온 감정의 흐름이야.")
            print("    이야기해 줘서 고마워. 언제든 다시 와 😊")
        break

    response = empathic_response(user_input)
    print("AI:", response)

