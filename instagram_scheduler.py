import requests
import ssl
import time

ssl._create_default_https_context = ssl._create_unverified_context

ACCESS_TOKEN = "REPLACE_TOKEN"
USER_ID = "17841429475486342"
GITHUB_USER = "today1onlyy-bit"
REPO_NAME = "today1only-videos"

FILENAMES = {
    5:  "05_몸이안움직이는날.mp4",
    6:  "06_이미늦었다고생각하는사람에게.mp4",
    7:  "07_오늘하나만할사람.mp4",
    8:  "08_완벽하게하려다아무것도못하는사람.mp4",
    9:  "09_밤마다후회하는사람에게.mp4",
    10: "10_나만뒤처진것같은사람에게.mp4",
    11: "11_계획만세우고끝나는사람.mp4",
    12: "12_아무것도하기싫은날.mp4",
    13: "13_시작이무서운이유.mp4",
    14: "14_오늘당신이미룬것하나만.mp4",
    15: "15_알면서도안하는사람.mp4",
    16: "16_검색만하다끝나는사람.mp4",
    17: "17_의욕다리지마세요.mp4",
    18: "18_머릿속이너무복잡한사람에게.mp4",
    19: "19_자꾸포기하는사람에게.mp4",
    20: "20_하루를다시시작하는법.mp4",
    21: "21_이영상본사람은하나만.mp4",
    22: "22_집중안되는사람에게.mp4",
    23: "23_할게너무많을때.mp4",
    24: "24_자신감없는사람에게.mp4",
    25: "25_계속비교하게되는사람.mp4",
    26: "26_불안해서못움직이는사람에게.mp4",
    27: "27_내일부터하려는사람에게.mp4",
    28: "28_오늘작은성공이필요한사람.mp4",
    29: "29_오늘하나만선언.mp4",
    30: "30_한달동안하나만해낸사람에게.mp4",
}

CAPTIONS = {
    5:  "몸이 안 움직이는 날 있잖아요.\n\n그날은 억지로 움직이면 안 돼요.\n대신 딱 한 가지만.\n\n자리에서 일어나는 것. 그것만.\n\n#오늘하루만 #동기부여 #자기계발 #shorts #마음챙김",
    6:  "지금 시작하기엔 늦었다고요?\n\n5년 후에도 똑같이 말할 거예요.\n'그때 시작할걸.'\n\n늦은 게 아니에요. 아직이에요.\n\n#오늘하루만 #동기부여 #자기계발 #shorts #마음챙김",
    7:  "오늘 할 일 열 개 적었죠?\n\n다 지우세요.\n딱 하나만 남기세요.\n\n하나를 끝낸 사람이 열 개를 시작한 사람보다 앞서 있어요.\n\n#오늘하루만 #동기부여 #자기계발 #shorts #마음챙김",
    8:  "완벽하게 하려다 아무것도 못 한 날,\n몇 번이나 됐어요?\n\n완벽한 시작은 없어요.\n어설프게 시작한 사람이 이겨요.\n\n#오늘하루만 #동기부여 #자기계발 #shorts #마음챙김",
    9:  "밤에 누우면 후회가 몰려오죠.\n'오늘도 그냥 보냈다.'\n\n그 감각이 느껴진다는 건\n아직 포기 안 했다는 뜻이에요.\n\n내일은 달라질 수 있어요.\n\n#오늘하루만 #동기부여 #자기계발 #shorts #마음챙김",
    10: "나만 뒤처진 것 같은 느낌 알아요?\n\nSNS는 남의 하이라이트만 보여줘요.\n당신은 남의 무대 뒤를 보면서\n내 일상이랑 비교하고 있는 거예요.\n\n당신 속도가 맞아요.\n\n#오늘하루만 #동기부여 #자기계발 #shorts #마음챙김",
    11: "노트에 계획 세우는 데 2시간,\n실행은 0분.\n\n이거 나 얘기인 사람 손.\n\n계획은 3줄이면 충분해요. 지금 바로 시작하세요.\n\n#오늘하루만 #동기부여 #자기계발 #shorts #마음챙김",
    12: "아무것도 하기 싫은 날 있잖아요.\n\n그날은 하지 마세요.\n대신 '쉬기로 결정했다'고 생각하세요.\n\n끌려가는 것과 선택하는 건 달라요.\n\n#오늘하루만 #동기부여 #자기계발 #shorts #마음챙김",
    13: "시작이 무서운 이유 알아요?\n\n잘 못할까봐가 아니에요.\n잘 하고 싶어서예요.\n\n그 마음이 있는 한 시작할 수 있어요.\n\n#오늘하루만 #동기부여 #자기계발 #shorts #마음챙김",
    14: "오늘 미룬 것 하나 떠올려보세요.\n\n그거 지금 3분만 해보세요.\n3분 후에 멈춰도 돼요.\n\n근데 아마 못 멈출 거예요.\n\n#오늘하루만 #동기부여 #자기계발 #shorts #마음챙김",
    15: "알면서도 안 하는 거,\n의지 문제가 아니에요.\n\n시작이 너무 크기 때문이에요.\n말도 안 되게 작게 쪼개세요.\n\n그게 시작이에요.\n\n#오늘하루만 #동기부여 #자기계발 #shorts #마음챙김",
    16: "유튜브 검색 2시간,\n인스타 레퍼런스 1시간,\n실행 0분.\n\n정보가 부족한 게 아니에요.\n시작이 부족한 거예요.\n\n#오늘하루만 #동기부여 #자기계발 #shorts #마음챙김",
    17: "의욕이 없어서 못 한다고요?\n\n반대예요.\n하면 의욕이 생겨요.\n\n의욕을 기다리지 마세요. 먼저 움직이세요.\n\n#오늘하루만 #동기부여 #자기계발 #shorts #마음챙김",
    18: "머릿속에 할 것들이 너무 많죠?\n\n지금 종이에 다 꺼내세요.\n머리 밖으로.\n\n비워야 움직일 수 있어요.\n\n#오늘하루만 #동기부여 #자기계발 #shorts #마음챙김",
    19: "또 포기했다고요?\n\n포기를 반복하는 사람은\n사실 계속 시도하는 사람이에요.\n\n포기하면서도 다시 보고 있잖아요. 그게 증거예요.\n\n#오늘하루만 #동기부여 #자기계발 #shorts #마음챙김",
    20: "하루가 망했다고 느껴질 때\n다시 시작하는 방법이 있어요.\n\n지금 이 순간부터 새 하루라고 선언하는 것.\n하루는 아침에만 시작되는 게 아니에요.\n\n#오늘하루만 #동기부여 #자기계발 #shorts #마음챙김",
    21: "이 영상 본 사람은 지금 당장\n딱 한 가지만 해보세요.\n\n뭐든 좋아요. 문자 하나, 메모 하나.\n\n본 김에 바꿔보는 거예요.\n\n#오늘하루만 #동기부여 #자기계발 #shorts #마음챙김",
    22: "집중이 안 되는 건 의지 문제가 아니에요.\n\n환경 문제예요.\n폰 엎어두고, 탭 닫고, 딱 하나만 띄우세요.\n\n집중은 만드는 거예요.\n\n#오늘하루만 #동기부여 #자기계발 #shorts #마음챙김",
    23: "할 게 너무 많을 때는\n아무것도 안 하게 되더라고요.\n\n목록에서 하나만 빼고 다 지우세요.\n그 하나만 오늘의 전부예요.\n\n#오늘하루만 #동기부여 #자기계발 #shorts #마음챙김",
    24: "자신감은 생기는 게 아니에요.\n\n뭔가를 해낸 다음에 따라오는 거예요.\n지금 자신감 없어도 괜찮아요.\n\n일단 하면 생겨요.\n\n#오늘하루만 #동기부여 #자기계발 #shorts #마음챙김",
    25: "또 비교했죠?\n\n그 사람은 당신이 보지 못한 시간을\n이미 보낸 거예요.\n\n당신도 지금 그 시간을 보내는 중이에요.\n\n#오늘하루만 #동기부여 #자기계발 #shorts #마음챙김",
    26: "불안해서 못 움직이는 거 알아요.\n\n근데 움직이지 않으면 불안이 사라질까요?\n더 커져요.\n\n불안한 채로 한 걸음. 그게 유일한 방법이에요.\n\n#오늘하루만 #동기부여 #자기계발 #shorts #마음챙김",
    27: "내일부터 하려는 사람에게 물어볼게요.\n\n어제도 내일부터라고 했죠?\n\n내일은 없어요. 오늘만 있어요.\n\n#오늘하루만 #동기부여 #자기계발 #shorts #마음챙김",
    28: "오늘 작은 성공 하나가 필요한 사람.\n\n지금 있는 자리에서 뭔가 하나만 정리하세요.\n책상 위 물건 하나.\n\n그 작은 것 하나가 오늘을 바꿔요.\n\n#오늘하루만 #동기부여 #자기계발 #shorts #마음챙김",
    29: "오늘 하루만 선언해보세요.\n\n'오늘 하루만, 나 한 번 제대로 살아본다.'\n\n내일은 몰라도 돼요. 오늘만.\n\n#오늘하루만 #동기부여 #자기계발 #shorts #마음챙김",
    30: "한 달 동안 하루하루 버텨온 당신에게.\n\n대단한 거 한 게 없는 것 같죠?\n\n매일 포기하지 않은 것,\n그게 제일 대단한 거예요.\n\n오늘 하루만, 그것만으로 충분합니다.\n\n#오늘하루만 #동기부여 #자기계발 #shorts #마음챙김",
}

def get_raw_url(num):
    filename = FILENAMES[num]
    encoded = requests.utils.quote(filename, safe="")
    return f"https://raw.githubusercontent.com/{GITHUB_USER}/{REPO_NAME}/main/{encoded}"

def create_container(video_url, caption):
    url = f"https://graph.instagram.com/v21.0/{USER_ID}/media"
    payload = {
        "media_type": "REELS",
        "video_url": video_url,
        "caption": caption,
        "access_token": ACCESS_TOKEN
    }
    r = requests.post(url, data=payload, verify=False)
    return r.json().get("id")

def check_status(container_id):
    url = f"https://graph.instagram.com/v21.0/{container_id}"
    params = {"fields": "status_code,status", "access_token": ACCESS_TOKEN}
    r = requests.get(url, params=params, verify=False)
    return r.json()

def publish(container_id):
    url = f"https://graph.instagram.com/v21.0/{USER_ID}/media_publish"
    payload = {"creation_id": container_id, "access_token": ACCESS_TOKEN}
    r = requests.post(url, data=payload, verify=False)
    return r.json()

def post_reel(num):
    caption = CAPTIONS[num]
    video_url = get_raw_url(num)
    print(f"[{num:02d}] 발행 시작: {FILENAMES[num]}")

    container_id = create_container(video_url, caption)
    if not container_id:
        print(f"[{num:02d}] 컨테이너 생성 실패")
        return False

    print(f"  처리 대기 중...")
    for i in range(30):
        time.sleep(10)
        status_data = check_status(container_id)
        status = status_data.get("status_code", "UNKNOWN")
        print(f"  {(i+1)*10}초: {status}")
        if status == "FINISHED":
            break
        if status == "ERROR":
            print(f"  오류: {status_data}")
            return False

    result = publish(container_id)
    print(f"[{num:02d}] 완료: {result}")
    return True

if __name__ == "__main__":
    import sys
    num = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    post_reel(num)
