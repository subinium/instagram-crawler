# Instagram Crawler 

## 설치
1. Chrome 브라우저가 설치되어 있어야 합니다.
2. [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/)를 다운로드 하고 bin 폴더에 넣어주세요:
`./inscrawler/bin/chromedriver`
3. Selenium을 설치해주세요: `pip3 install -r requirements.txt`
4. `cp inscrawler/secret.py.dist inscrawler/secret.py`

당신의 사용자 이름/비밀번호를 `secret.py`에 설정하거나 환경 변수에 설정하세요.

### 사용
```
python late_hashtag_crawling.py -st 0 -ed 100 -s 10
```

- st : start index
- ed : end index
- s : 만약을 대비한 중간 저장 term 설정