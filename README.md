loginsrv-minimal
===

loginsrv: https://github.com/tarent/loginsrv

### Usage

- GitHub OAuth setting
  - Homepage URL: http://localhost
  - Authorization callback URL: http://localhost/login/github

```
$ https://github.com/altescy/loginsrv-minimal.git
$ cd loginsrv-minimal
$ cat << EOF > .env
LOGINSRV_JWT_ALGO=HS512
LOGINSRV_JWT_SECRET=[ YOUR JWT SECRET ]
LOGINSRV_SIMPLE=bob=secret
LOGINSRV_SUCCESS_URL=http://localhost/after
LOGINSRV_GITHUB=client_id=[ YOUR CLIENT ID ],client_secret=[ YOUR SECRET ]
EOF
$ docker-compose up -d
```
