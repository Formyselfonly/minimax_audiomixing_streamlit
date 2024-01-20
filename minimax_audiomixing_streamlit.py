import requests
import streamlit as st
import base64
st.title("AI伴游-角色混音Demo")

gender=st.sidebar.selectbox("选择角色性别",["男","女"])
st.sidebar.image("sidebar_show.jpg", caption='开玩开玩!')


if gender=="男":
    st.info("自由拖动滑杆,创造你的专属男角色音线")
    male_qn_qingse = st.slider("正太", 1, 100, 1)
    male_qn_jingying = st.slider("成熟", 1, 100, 100)
    male_qn_badao = st.slider("霸道", 1, 100, 1)
    male_qn_daxuesheng = st.slider("阳光", 1, 100, 1)

    # 这两个下一步再改,默认的问题也不大
    speed = 0.7
    vol = 1.0
    group_id = "1689852985712348"
    api_key = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJOYW1lIjoidGVzdCIsIlN1YmplY3RJRCI6IjE2ODk4NTI5ODU1OTczOTIiLCJQaG9uZSI6Ik1UVTRNVFU0TURJNU1qUT0iLCJHcm91cElEIjoiMTY4OTg1Mjk4NTcxMjM0OCIsIlBhZ2VOYW1lIjoiIiwiTWFpbCI6InpseWdpbGlhbmFAc2luYS5jb20iLCJDcmVhdGVUaW1lIjoiMjAyMy0wOS0wNSAwMDoyNjo1NSIsImlzcyI6Im1pbmltYXgifQ.gdr3NXX8bAKN9E0bzuVsX5HhGXfHnZRY7YEjzo36_CYXUSDDZ4ZZTTopRJ1SLo9O_bOXJ0pnw2FJHz4kVvOedHbrBXbXHAFwyjWZfZ1kP0iE_n11EEClyIXizUvrh35m1DjPhMiPMYXJpVWy5dIkcD7UHBpZCw3DRk68I8XxdkFkZ3LHmBNqvbH9isTRiCzXUprnk2FwfrU8y38-K-H0mzhzJwxNYCO7SuOr26ZBJGDfPGS8K-X2WCJSYUH6pWwocGBrT10Du4A5qH03Eri0xQ4zs1O08G8tYkp4vWhdcNo7iXMDwGeV-BT5yFup6toAFu7CoU-ge30szOv-6AMsSw"

    text = st.text_area('输入文本',  "爱像一阵风,吹完它就走,这样的节奏,谁都无可奈何,没有妳以后,我灵魂失控,黑云在降落,我被它拖着走,静静,悄悄,默默,离开,陷入了危险边缘")
    if st.button('文本转语音'):
        url = f"https://api.minimax.chat/v1/text_to_speech?GroupId={group_id}"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }

        data = {
            "text": text,
            "model": "speech-01",
            "speed": speed,
            "vol": vol,
            "pitch": 0,
            "timber_weights": [
                {
                    "voice_id": "male-qn-qingse",
                    "weight": male_qn_qingse
                },
                {
                    "voice_id": "male-qn-jingying",
                    "weight": male_qn_jingying
                },
                {
                    "voice_id": "male-qn-badao",
                    "weight": male_qn_badao
                },
                {
                    "voice_id": "male-qn-daxuesheng",
                    "weight": male_qn_daxuesheng
                },
            ]
        }

        response = requests.post(url, headers=headers, json=data)
        print("trace_id", response.headers.get("Trace-Id"))
        if response.status_code == 200:
            with open("output.mp3", "wb") as f:
                f.write(response.content)
            st.success('Conversion successful!')
            st.balloons()
            # st.audio("output.mp3", format='audio/mp3')
            with open("output.mp3", "rb") as f:
                audio_bytes = f.read()
            audio_b64 = base64.b64encode(audio_bytes).decode()
            href = f'<a href="data:audio/mp3;base64,{audio_b64}" download="output.mp3">点击下载</a>'
            st.markdown(href, unsafe_allow_html=True)

            st.audio(audio_bytes, format="audio/mp3")

        else:
            st.error('Failed to convert text to speech.')


elif gender=="女":
    st.info("自由拖动滑杆,创造你的专属女角色音线")
    female_shaonv = st.slider("少女", 1, 100, 1)
    female_yujie = st.slider("御姐", 1, 100, 1)
    female_chengshu = st.slider("成熟", 1, 100, 100)
    female_tianmei = st.slider("甜美", 1, 100, 1)

    text = st.text_area("输入文本",
                        "爱像一阵风,吹完它就走,这样的节奏,谁都无可奈何,没有妳以后,我灵魂失控,黑云在降落,我被它拖着走,静静,悄悄,默默,离开,陷入了危险边缘")

    group_id = "1689852985712348"
    api_key = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJOYW1lIjoidGVzdCIsIlN1YmplY3RJRCI6IjE2ODk4NTI5ODU1OTczOTIiLCJQaG9uZSI6Ik1UVTRNVFU0TURJNU1qUT0iLCJHcm91cElEIjoiMTY4OTg1Mjk4NTcxMjM0OCIsIlBhZ2VOYW1lIjoiIiwiTWFpbCI6InpseWdpbGlhbmFAc2luYS5jb20iLCJDcmVhdGVUaW1lIjoiMjAyMy0wOS0wNSAwMDoyNjo1NSIsImlzcyI6Im1pbmltYXgifQ.gdr3NXX8bAKN9E0bzuVsX5HhGXfHnZRY7YEjzo36_CYXUSDDZ4ZZTTopRJ1SLo9O_bOXJ0pnw2FJHz4kVvOedHbrBXbXHAFwyjWZfZ1kP0iE_n11EEClyIXizUvrh35m1DjPhMiPMYXJpVWy5dIkcD7UHBpZCw3DRk68I8XxdkFkZ3LHmBNqvbH9isTRiCzXUprnk2FwfrU8y38-K-H0mzhzJwxNYCO7SuOr26ZBJGDfPGS8K-X2WCJSYUH6pWwocGBrT10Du4A5qH03Eri0xQ4zs1O08G8tYkp4vWhdcNo7iXMDwGeV-BT5yFup6toAFu7CoU-ge30szOv-6AMsSw"
    speed = 1.0
    vol = 1.0

    if st.button("文本转语音"):
        url = f"https://api.minimax.chat/v1/text_to_speech?GroupId={group_id}"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
        data = {
            # "voice_id": "female-yujie-jingpin",
            # 如同时传入voice_id和timber_weights时，则会自动忽略voice_id，以timber_weights传递的参数为准
            "text": text,
            "model": "speech-01",
            "speed": speed,
            "vol": vol,
            "pitch": 0,
            "timber_weights": [

                {
                    "voice_id": "female-shaonv",
                    "weight": female_shaonv
                },
                {
                    "voice_id": "female-yujie",
                    "weight": female_yujie
                },
                {
                    "voice_id": "female-chengshu",
                    "weight": female_chengshu
                },
                {
                    "voice_id": "female-tianmei",
                    "weight": female_tianmei
                },

            ]
        }

        response = requests.post(url, headers=headers, json=data)
        print("trace_id", response.headers.get("Trace-Id"))
        if response.status_code == 200:
            with open("output.mp3", "wb") as f:
                f.write(response.content)
            st.success("转换成功!")
            st.balloons()
            # st.audio("output.mp3", format="audio/mp3")
            with open("output.mp3", "rb") as f:
                audio_bytes = f.read()
            audio_b64 = base64.b64encode(audio_bytes).decode()
            href = f'<a href="data:audio/mp3;base64,{audio_b64}" download="output.mp3">点击下载</a>'
            st.markdown(href, unsafe_allow_html=True)

            st.audio(audio_bytes, format="audio/mp3")
        else:
            st.error("出错了,请查看报错信息!")

#

else:
    st.write("请选择性别")