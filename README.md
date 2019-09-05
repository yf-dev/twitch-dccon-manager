# Twitch Dccon Manager

:warning: 이 프로젝트는 현재 개발 단계로, 실 사용이 불가능합니다. :warning:

Twitch Dccon Manager는 [Bridge BBCC](https://github.com/krynen/BridgeBBCC),
[ChatAssistX-Client](https://github.com/Lastorder-DC/ChatAssistX-Client)와 같이 디시콘을 지원하는 채팅 오버레이를 위한
디시콘 관리 서비스입니다.

제공하는 기능은 다음과 같습니다.

- Twitch 계정으로 로그인
- ~~디시콘 관리용 Github 저장소 생성~~
- ~~디시콘 목록에 디시콘 추가/수정/삭제~~
- ~~시청자용 디시콘 리스트 페이지~~
- ~~Bridge BBCC, ChatAssistX-Client용 디시콘 설정 내보내기~~
- ~~[Twitch DCCON extension](https://chrome.google.com/webstore/detail/twitch-dccon-extension/nljojmgmnidbehhocgkbeejchcmkpgki?hl=ko) 연동~~


## Project setup

``` bash
docker-compose -f .\backend\docker-compose.dev.yml build
```

### Run service for development

[settings.env.example](./settings.env.example) 파일을 복사하여 settings.dev.env 파일을 적절히 작성합니다.

``` bash
# init database
docker-compose -f .\backend\docker-compose.dev.yml run --rm backend pipenv run python manage.py db upgrade
# run backend
docker-compose -f .\backend\docker-compose.dev.yml up backend
# run frontend
docker-compose -f .\frontend\docker-compose.dev.yml up frontend
```

### Run service for production

[settings.env.example](./settings.env.example) 파일을 복사하여 settings.env 파일을 적절히 작성합니다.

``` bash
docker-compose -f .\frontend\docker-compose.prod.yml run --rm frontend yarn run build
docker-compose -f .\backend\docker-compose.prod.yml up -d backend
```

## License

MIT