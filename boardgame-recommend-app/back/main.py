from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Board Game Recommendation Engine API")

class UserInput(BaseModel):
    player_count: str
    playing_time: str
    difficulty: str
    atmosphere: str
    mechanism: str

class GameDetail(BaseModel):
    game_name: str
    score: int
    catchphrase: str
    tags: List[str]
    recommended_for: str
    setup_info: str
    rules: List[str]

class RecommendResponse(BaseModel):
    games: List[GameDetail]

BOARDGAME_DB = [
    {
        "name": "루미큐브",
        "best_players": "3~4인", "time": "적당하게 (30분~1시간)", 
        "difficulty": "초보자용 (설명 시간 5분)",
        "atmosphere": "두뇌 싸움 (치열한 전략)", "mechanism": "덱빌딩 및 자원관리 (자원 소모)",
        "catchphrase": "숫자 등록의 짜릿함! 전 세계가 즐기는 두뇌 회전 보드게임",
        "recommended_for": "가족, 친구들과 깔끔하고 정적인 두뇌 회전을 즐기고 싶을 때",
        "setup_info": "룰 설명에 걸리는 시간: 5분 ｜ 한 판당 평균 시간: 30분",
        "rules": ["1. 숫자 타일 14장씩 나누어 갖기", "2. 규칙에 맞게 바닥에 숫자 조합 등록하기", "3. 내 손의 타일을 가장 먼저 모두 털어내면 승리!"]
    },
    {
        "name": "할리갈리",
        "best_players": "3~4인", "time": "짧고 굵게 (30분 미만)", 
        "difficulty": "초보자용 (설명 시간 5분)",
        "atmosphere": "파티피플 (웃고 떠드는 분위기)", "mechanism": "순발력 및 피지컬",
        "catchphrase": "과일 5개가 보이면 종을 울려라! 국민 보드게임",
        "recommended_for": "어색한 분위기를 깨고 엄청난 웃음과 짜릿한 스피드를 즐기고 싶을 때",
        "setup_info": "룰 설명에 걸리는 시간: 1분 ｜ 한 판당 평균 시간: 15분",
        "rules": ["1. 카드를 한 장씩 순서대로 뒤집는다", "2. 같은 과일이 5개가 되는 순간 종을 친다", "3. 가장 먼저 종을 친 사람이 바닥의 카드를 모두 가져간다"]
    },
    {
        "name": "스플렌더",
        "best_players": "3~4인", "time": "적당하게 (30분~1시간)", "difficulty": "중급자용 (약간의 전략 필요)",
        "atmosphere": "두뇌 싸움 (치열한 전략)", "mechanism": "덱빌딩 및 자원관리 (자원 소모)",
        "catchphrase": "보석을 모아 귀족의 마음을 사로잡아라! 본격 자원관리 전략 게임",
        "recommended_for": "정적이고 치열하게 보석 자원을 모아 나만의 빌드업을 완성하고 싶을 때",
        "setup_info": "룰 설명에 걸리는 시간: 10분 ｜ 한 판당 평균 시간: 40분",
        "rules": ["1. 차례마다 보석 토큰을 가져오거나 개발 카드를 구입한다", "2. 구매한 카드로 더 비싼 카드의 할인 혜택을 받는다", "3. 개발 카드와 귀족 점수의 합이 15점 이상이면 승리!"]
    },
    {
        "name": "아발론 (레지스탕스 아발론)",
        "best_players": "5인 이상", "time": "적당하게 (30분~1시간)", "difficulty": "중급자용 (약간의 전략 필요)",
        "atmosphere": "두뇌 싸움 (치열한 전략)", "mechanism": "블러핑 (속고 속이는 마피아)",
        "catchphrase": "정의와 사악함의 대결! 마피아 게임의 끝판왕",
        "recommended_for": "친구들의 완벽한 포커페이스를 무너뜨리고 소름 돋는 심리전을 펼치고 싶을 때",
        "setup_info": "룰 설명에 걸리는 시간: 15분 ｜ 한 판당 평균 시간: 45분",
        "rules": ["1. 선과 악의 진영으로 역할을 비밀리에 나누어 갖는다", "2. 원정을 떠날 팀을 구성하고 투표를 통해 원정을 진행한다", "3. 선은 원정 3회 성공, 악은 원정 3회 실패 또는 멀린 암살 시 승리!"]
    },
    {
        "name": "뱅! (BANG!)",
        "best_players": "5인 이상", "time": "적당하게 (30분~1시간)", "difficulty": "중급자용 (약간의 전략 필요)",
        "atmosphere": "파티피플 (웃고 떠드는 분위기)", "mechanism": "블러핑 (속고 속이는 마피아)",
        "catchphrase": "서부의 무법지대, 서로에게 총구를 겨눠라!",
        "recommended_for": "누가 내 편인지 모르는 상황에서 서부의 총잡이가 되어 유쾌하게 싸우고 싶을 때",
        "setup_info": "룰 설명에 걸리는 시간: 10분 ｜ 한 판당 평균 시간: 30분",
        "rules": ["1. 보안관, 부관, 무법자, 배신자 카드를 안 보이게 나눠 갖는다", "2. 내 턴에 카드를 뽑아 장비를 장착하거나 다른 플레이어를 사격한다", "3. 각 직업의 비밀 승리 조건(예: 무법자는 보안관 제거)을 달성하면 승리!"]
    },
    {
        "name": "젠가",
        "best_players": "2인", "time": "짧고 굵게 (30분 미만)", "difficulty": "초보자용 (설명 시간 5분)",
        "atmosphere": "아이스브레이킹 (어색한 사이)", "mechanism": "순발력 및 피지컬",
        "catchphrase": "아슬아슬한 중력과의 싸움! 손끝으로 전해지는 스릴",
        "recommended_for": "대화가 조심스러운 초면이거나, 벌칙 게임용 초간단 피지컬 게임이 필요할 때",
        "setup_info": "룰 설명에 걸리는 시간: 30초 ｜ 한 판당 평균 시간: 10분",
        "rules": ["1. 나무 블록을 3개씩 교차하여 탑을 높게 쌓는다", "2. 한 손만 사용하여 원하는 층의 블록을 조심스럽게 하나 빼낸다", "3. 뺀 블록을 맨 위에 쌓아 올리며, 탑을 무너뜨리는 사람이 패배!"]
    },
    {
        "name": "테라포밍 마스",
        "best_players": "3~4인", "time": "본격적으로 (1시간 이상)", "difficulty": "고인물용 (설명만 30분)",
        "atmosphere": "두뇌 싸움 (치열한 전략)", "mechanism": "덱빌딩 및 자원관리 (자원 소모)",
        "catchphrase": "인류의 새로운 고향, 화성을 녹색 행성으로 개척하라",
        "recommended_for": "보드게임에 진심인 고수들과 헤비하고 깊이 있는 인프라 구축 전략을 펼치고 싶을 때",
        "setup_info": "룰 설명에 걸리는 시간: 30분 ｜ 한 판당 평균 시간: 120분",
        "rules": ["1. 기업을 선택하고 매 라운드 다양한 프로젝트 카드를 구매한다", "2. 자원을 생산하여 화성의 온도, 산소도, 해양 조건을 올린다", "3. 화성 환경 점수와 기업 점수를 합산하여 가장 높은 점수가 승리!"]
    },
    {
        "name": "5초 준다!",
        "best_players": "3~6인", "time": "짧고 굵게 (30분 미만)", "difficulty": "초보자용 (설명 시간 5분)",
        "atmosphere": "아이스브레이킹 (어색함 타파)", "mechanism": "순발력 및 피지컬 (속도전)",
        "catchphrase": "머리가 하얘지는 5초의 마법! 순발력 끝판왕 질문 게임",
        "recommended_for": "어색한 분위기를 빠르게 깨고 다 함께 웃으며 시작하고 싶을 때",
        "setup_info": "룰 설명에 걸리는 시간: 2분 ｜ 한 판당 평균 시간: 15~20분",
        "rules": ["1. 카드를 한 장 뽑아 질문을 확인한다", "2. 타이머가 작동하면 5초 안에 정답 3가지를 외친다", "3. 성공하면 카드를 획득하고, 실패하면 다음 사람에게 기회가 넘어간다"]
    },
    {
        "name": "달무티",
        "best_players": "5~8인", "time": "적당하게 (30분~1시간)", "difficulty": "초보자용 (설명 시간 5분)",
        "atmosphere": "파티피플 (소란스러운 분위기)", "mechanism": "손패 털기 (계급 전쟁)",
        "catchphrase": "영원한 왕도, 영원한 노예도 없다! 본격 신분 계급 역전 게임",
        "recommended_for": "인원이 많고, 서로 장난치며 왁자지껄한 분위기를 만들고 싶을 때",
        "setup_info": "룰 설명에 걸리는 시간: 5분 ｜ 한 판당 평균 시간: 15~30분",
        "rules": ["1. 등수에 따라 왕, 귀족, 평민, 노예 등의 계급을 나눈다", "2. 앞 사람이 낸 카드보다 같은 장수이면서 더 낮은 숫자의 카드를 낸다", "3. 손의 카드를 먼저 턴 순서대로 다음 판의 계급이 결정된다"]
    },
    {
        "name": "코드네임",
        "best_players": "4~8인", "time": "적당하게 (30분~1시간)", "difficulty": "초보자용 (설명 시간 5분)",
        "atmosphere": "파티피플 (소란스러운 분위기)", "mechanism": "단어 연상 및 팀전",
        "catchphrase": "단 하나의 단어로 팀을 이끌어라! 스파이 마스터의 암호 해독 게임",
        "recommended_for": "팀을 나누어 센스와 공감대를 시험해보고 싶을 때",
        "setup_info": "룰 설명에 걸리는 시간: 5분 ｜ 한 판당 평균 시간: 30분",
        "rules": ["1. 레드 팀과 블루 팀으로 나누고 각 팀의 팀장을 뽑는다", "2. 팀장은 바닥의 단어들을 연상시킬 수 있는 '단 한 단어와 숫자'로 힌트를 준다", "3. 팀원들은 암살자를 피하되, 상대 팀보다 먼저 우리 팀의 스파이 단어를 모두 찾아야 한다"]
    },
    {
        "name": "꼬치의 달인",
        "best_players": "2~4인", "time": "짧고 굵게 (30분 미만)", "difficulty": "초보자용 (설명 시간 5분)",
        "atmosphere": "파티피플 (소란스러운 분위기)", "mechanism": "순발력 및 피지컬 (속도전)",
        "catchphrase": "눈보다 손이 빨라야 한다! 맛있는 꼬치구이 컴포넌트 게임",
        "recommended_for": "룰 설명을 듣기 싫어하고 몸으로 부딪히는 실시간 게임을 원할 때",
        "setup_info": "룰 설명에 걸리는 시간: 3분 ｜ 한 판당 평균 시간: 15분",
        "rules": ["1. 각자 막대 하나와 토핑 재료들을 나눠 갖는다", "2. 주문서 카드가 뒤집히면 그림과 똑같은 순서로 재료를 막대에 꽂는다", "3. 가장 먼저 완성하고 '맛있게 드세요!'를 외친 사람이 점수를 얻는다"]
    },
    {
        "name": "레지스탕스 아발론",
        "best_players": "5~10인", "time": "적당하게 (30분~1시간)", "difficulty": "중급자용 (약간의 전략 필요)",
        "atmosphere": "블러핑 (속고 속이는 마피아)", "mechanism": "비밀 투표 및 역할 연기",
        "catchphrase": "누가 정의이고 누가 악인가? 마피아 게임의 마스터피스",
        "recommended_for": "서로 말을 많이 대화하며 완벽한 포커페이스와 추리력을 겨루고 싶을 때",
        "setup_info": "룰 설명에 걸리는 시간: 15분 ｜ 한 판당 평균 시간: 45분",
        "rules": ["1. 아서왕의 신하(선)와 모드레드의 하수인(악)으로 정체를 숨겨 역할을 받는다", "2. 원정대를 꾸려 원정을 보낼지 말지 비밀 투표를 진행한다", "3. 선 진역은 원정 3회 성공을, 악 진역은 원정 3회 실패 또는 멀린 암살을 노린다"]
    },
    {
        "name": "스파이폴",
        "best_players": "4~8인", "time": "짧고 굵게 (30분 미만)", "difficulty": "초보자용 (설명 시간 5분)",
        "atmosphere": "블러핑 (속고 속이는 마피아)", "mechanism": "질문과 답변 (토크형 부류)",
        "catchphrase": "너 지금 어디야? 질문 속에 가시를 숨긴 스파이 색출 작전",
        "recommended_for": "마피아 게임에서 밤마다 눈감는 시간이 지루했던 사람들에게",
        "setup_info": "룰 설명에 걸리는 시간: 5분 ｜ 한 판당 평균 시간: 10~15분",
        "rules": ["1. 한 명의 스파이를 제외하고 모두 같은 장소가 적힌 카드를 받는다", "2. 서로 장소에 관련된 질문과 답변을 번갈아 가며 주고받는다", "3. 시민들은 스파이를 찾아내야 하고, 스파이는 들키지 않거나 장소를 맞추면 승리한다"]
    },
    {
        "name": "리어스 다이스",
        "best_players": "3~6인", "time": "짧고 굵게 (30분 미만)", "difficulty": "초보자용 (설명 시간 5분)",
        "atmosphere": "블러핑 (속고 속이는 마피아)", "mechanism": "주사위 굴리기 및 확률 예측",
        "catchphrase": "캐리비안의 해적들이 즐기던 그 게임! 배짱과 확률의 주사위 대결",
        "recommended_for": "간단한 컴포넌트로 극도의 긴장감과 심리전을 느끼고 싶을 때",
        "setup_info": "룰 설명에 걸리는 시간: 5분 ｜ 한 판당 평균 시간: 20분",
        "rules": ["1. 주사위 5개를 컵에 넣고 흔든 뒤 나만 확인한다", "2. 게임판 전체에 특정 주사위 눈이 총 몇 개 이상 있을지 벳(Bet)을 한다", "3. 앞 사람의 말이 거짓말 같으면 '구라(Liar)'를 외쳐 주사위를 공개하고 틀린 사람이 주사위를 잃는다"]
    },
    {
        "name": "카르카손",
        "best_players": "2~4인", "time": "적당하게 (30분~1시간)", "difficulty": "초보자용 (설명 시간 5분)",
        "atmosphere": "두뇌 싸움 (치열한 전략)", "mechanism": "타일 배치 및 영향력 싸움",
        "catchphrase": "내 손으로 만드는 중세 도시! 전 세계가 사랑하는 타일 배치 게임",
        "recommended_for": "보드판이 매번 다르게 완성되는 아름다운 성과 길을 만들고 싶을 때",
        "setup_info": "룰 설명에 걸리는 시간: 5분 ｜ 한 판당 평균 시간: 35~40분",
        "rules": ["1. 보이지 않는 주머니에서 지형 타일을 하나 뽑아 바닥에 연결되게 놓는다", "2. 놓은 타일의 길, 성, 수도원에 내 부하(미플)를 배치해 소유권을 주장한다", "3. 성이나 길이 완성되면 미플을 회수하며 점수를 획득한다"]
    },
    {
        "name": "카탄",
        "best_players": "3~4인", "time": "본격적으로 (1시간 이상)", "difficulty": "중급자용 (약간의 전략 필요)",
        "atmosphere": "두뇌 싸움 (치열한 전략)", "mechanism": "자원 교환 및 네트워크 빌딩",
        "catchphrase": "무인도를 개척할 최고의 영주를 찾습니다! 보드게임의 살아있는 전설",
        "recommended_for": "단순한 운을 넘어 플레이어 간의 활발한 협상과 거래를 즐기고 싶을 때",
        "setup_info": "룰 설명에 걸리는 시간: 15분 ｜ 한 판당 평균 시간: 60~90분",
        "rules": ["1. 주사위 두 개를 굴려 나온 숫자의 땅에서 생산되는 자원(나무, 흙 등)을 획득한다", "2. 나에게 없는 자원은 다른 플레이어와 자유롭게 협상하여 물물교환한다", "3. 자원을 소모해 길과 마을, 도시를 건설하여 먼저 10점을 얻으면 승리한다"]
    },
    {
        "name": "윙스팬",
        "best_players": "1~4인", "time": "본격적으로 (1시간 이상)", "difficulty": "중급자용 (약간의 전략 필요)",
        "atmosphere": "두뇌 싸움 (치열한 전략)", "mechanism": "덱빌딩 및 자원관리 (엔진 빌딩)",
        "catchphrase": "나만의 아름다운 새 생태계를 가꾸다! 소장 가치 100% 힐링 전략 게임",
        "recommended_for": "예쁜 일러스트를 보며 내 차례에 강력한 시너지를 내는 콤보 플레이를 원할 때",
        "setup_info": "룰 설명에 걸리는 시간: 20분 ｜ 한 판당 평균 시간: 60분",
        "rules": ["1. 매 턴 새 카드 얻기, 먹이 얻기, 알 낳기, 새 플레이하기 중 하나의 액션을 한다", "2. 서식지에 새를 놓을 때마다 해당 서식지의 액션 효율이 점점 강력해진다", "3. 4라운드 동안 새 점수, 보너스 카드 점수, 라운드 목표 점수를 합산해 승자를 가린다"]
    },
    {
        "name": "아줄",
        "best_players": "2~4인", "time": "적당하게 (30분~1시간)", "difficulty": "초보자용 (설명 시간 5분)",
        "atmosphere": "두뇌 싸움 (치열한 전략)", "mechanism": "타일 드래프팅 및 패턴 완성",
        "catchphrase": "왕궁의 벽면을 수놓는 화려한 타일 공예! 치열한 수 싸움의 미학",
        "recommended_for": "눈이 즐거운 고품질 컴포넌트와 상대방을 견제하는 딴지 재미를 동시에 챙기고 싶을 때",
        "setup_info": "룰 설명에 걸리는 시간: 5분 ｜ 한 판당 평균 시간: 30~40분",
        "rules": ["1. 진열대에서 원하는 색상의 타일을 모두 가져오고, 남은 타일은 중앙으로 보낸다", "2. 가져온 타일을 내 개인 판의 대기선에 규칙에 맞게 배치한다", "3. 라운드가 끝날 때 대기선이 가득 찬 타일을 벽면으로 옮겨 점수를 얻고 패턴을 완성한다"]
    },
    {
        "name": "스플렌더 대결",
        "best_players": "2인 전용", "time": "적당하게 (30분~1시간)", "difficulty": "중급자용 (약간의 전략 필요)",
        "atmosphere": "두뇌 싸움 (치열한 전략)", "mechanism": "자원 소모 및 셋 컬렉션",
        "catchphrase": "오직 단 둘만을 위해 태어났다! 더 콤팩트하고 치열해진 명작의 귀환",
        "recommended_for": "연인이나 절친 등 정확히 2명이서 밀도 높은 긴장감의 두뇌 싸움을 하고 싶을 때",
        "setup_info": "룰 설명에 걸리는 시간: 10분 ｜ 한 판당 평균 시간: 30분",
        "rules": ["1. 공동 보드판에서 연속된 형태의 보석 토큰을 최대 3개까지 가져온다", "2. 모은 보석 토큰을 지불하고 능력과 점수가 있는 보석 카드를 구매한다", "3. 카드 구매 시 보석 할인 혜택을 받으며 총점 20점 등 3가지 승리 조건 중 하나를 먼저 달성한다"]
    }
]

@app.post("/recommend", response_model=RecommendResponse)
def get_recommendation(data: UserInput):
    scored_games = []
    
    for game in BOARDGAME_DB:
        match_points = 0
        total_criteria = 5
        
        if game["best_players"] == data.player_count: match_points += 1
        if game["time"] == data.playing_time: match_points += 1
        if game["difficulty"] == data.difficulty: match_points += 1
        if game["atmosphere"] == data.atmosphere: match_points += 1
        if game["mechanism"] == data.mechanism: match_points += 1
        
        score_percentage = int((match_points / total_criteria) * 100)
        if score_percentage == 0: score_percentage = 45
        elif score_percentage == 100: score_percentage = 98
        else: score_percentage = min(score_percentage + 15, 92)
            
        scored_games.append({
            "game_name": game["name"],
            "score": score_percentage,
            "catchphrase": game["catchphrase"],
            "tags": [game["best_players"], game["time"], game["difficulty"]],
            "recommended_for": game["recommended_for"],
            "setup_info": game["setup_info"],
            "rules": game["rules"]
        })
        
    sorted_games = sorted(scored_games, key=lambda x: x["score"], reverse=True)[:3]
    
    return {"games": sorted_games}