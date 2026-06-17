import streamlit as st
import requests

st.set_page_config(page_title="보드게임 맞춤 추천 큐레이터", page_icon="🎲", layout="centered")

st.title("🎲 오늘 만나볼 인생 보드게임은?")
st.caption("인원수, 플레이 시간, 성향을 분석하여 오늘 모임 분위기를 하드캐리할 TOP 3 보드게임을 추천합니다.")
st.markdown("---")

st.subheader("🎯필수 조건을 입력 해주세요")
col1, col2 = st.columns(2)

with col1:
    player_count = st.selectbox(
        "플레이할 정확한 인원은 몇 명인가요?", 
        ["2인", "2인 전용", "2~4인", "3~4인", "3~6인", "4~8인", "5~8인", "5~10인"]
    )
with col2:
    playing_time = st.selectbox(
        "사용 가능한 가용 시간은 어느 정도인가요?", 
        ["짧고 굵게 (30분 미만)", "적당하게 (30분~1시간)", "본격적으로 (1시간 이상)"]
    )

st.markdown(" ")
st.subheader("🎯취향 및 모임 성향 필터링")

difficulty = st.radio(
    "보드게임 숙련도 (난이도)를 선택하세요", 
    ["초보자용 (설명 시간 5분)", "중급자용 (약간의 전략 필요)", "고인물용 (설명만 30분)"]
)

col3, col4 = st.columns(2)
with col3:
    atmosphere = st.selectbox(
        "오늘 모임의 분위기는 어떤가요?", 
        [
            "🎮아이스브레이킹 (어색함 타파)", 
            "🏟️파티피플 (소란스러운 분위기)", 
            "🤼두뇌 싸움 (치열한 전략)", 
            "⚔️블러핑 (속고 속이는 마피아)"
        ]
    )
with col4:
    mechanism = st.selectbox(
        "🎯선호하는 핵심 재미 요소(메커니즘)는?", 
        [
            "순발력 및 피지컬 (속도전)", 
            "손패 털기 (계급 전쟁)", 
            "단어 연상 및 팀전", 
            "비밀 투표 및 역할 연기", 
            "질문과 답변 (토크형 부류)", 
            "주사위 굴리기 및 확률 예측", 
            "타일 배치 및 영향력 싸움", 
            "자원 교환 및 네트워크 빌딩", 
            "덱빌딩 및 자원관리 (엔진 빌딩)", 
            "타일 드래프팅 및 패턴 완성", 
            "자원 소모 및 셋 컬렉션"
        ]
    )

st.markdown("---")

if st.button("✨ 오늘 모임 맞춤 보드게임 찾기"):
    backend_url = "http://back:8000/recommend"
    
    payload = {
        "player_count": player_count,
        "playing_time": playing_time,
        "difficulty": difficulty,
        "atmosphere": atmosphere,
        "mechanism": mechanism
    }
    
    try:
        with st.spinner("가중치 매칭 알고리즘 기반 보드게임 데이터 연산 중..."):
            response = requests.post(backend_url, json=payload)
            
        if response.status_code == 200:
            result = response.json()
            
            if not result.get("games"):
                st.warning("⚠️ 선택하신 조건과 매칭되는 보드게임이 데이터베이스에 없습니다. 조건을 조금 변경해 보세요!")
            else:
                st.success("🎉 오늘 모임과 찰떡궁합인 보드게임 TOP 3 결과가 도출되었습니다!")
                st.markdown(" ")
                
                for idx, game in enumerate(result["games"]):
                    with st.container():
                        st.markdown(f"### 🏆 TOP {idx+1} : {game['book_title']}")
                        st.write(f"📊 **오늘 모임과 {game['score']}% 일치!**")
                        st.info(f"💡 \"{game['catchphrase']}\"")
                        
                        tags_str = " ｜ ".join([f"`{tag}`" for tag in game["tags"]])
                        st.markdown(tags_str)
                        
                        with st.expander("🔍 상세 정보 및 간단한 핵심 룰 보기"):
                            st.markdown(f"🎯 **이런 분들에게 추천해요:**\n\n{game['recommended_for']}")
                            st.markdown(f"⏱️ **체감 장벽 데이터:**\n\n{game['setup_info']}")
                            
                            st.markdown(" ")
                            st.markdown("**💡 핵심 룰 요약**")
                            for rule in game["rules"]:
                                st.write(rule)
                    st.markdown("---")
        else:
            st.error("백엔드 매칭 엔진과의 데이터 규격 통신에 오류가 발생했습니다.")
            
    except requests.exceptions.ConnectionError:
        st.error("FastAPI 백엔드 컨테이너 서버에 연결할 수 없습니다. Docker 가동 상태를 확인하세요.")