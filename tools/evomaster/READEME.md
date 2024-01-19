### Usage
petstore
java -jar evomaster.jar --blackBox true --bbSwaggerUrl  http://localhost:8080/api/v3/openapi.json --bbTargetUrl http://localhost:8080 --outputFormat JAVA_JUNIT_4 --maxTime 10m --outputFolder  petstore

languagetool
java -jar evomaster.jar --blackBox true --bbSwaggerUrl  https://languagetool.org/http-api/languagetool-swagger.json --bbTargetUrl http://localhost:8010 --outputFormat JAVA_JUNIT_4 --maxTime 10m --outputFolder  petstore

Vampi:
java -jar evomaster.jar --blackBox true --bbSwaggerUrl file:///root/REST_Go/services/VAmPI/openapi_specs/openapi3.yml --outputFormat JAVA_JUNIT_4 --outputFolder vampi --bbTargetUrl http://localhost:5000 --maxTime 10m

erc_20
java -jar evomaster.jar --blackBox true --bbSwaggerUrl file:///root/REST_Go/services/erc20-rest-service/erc_20_3.0.json --outputFormat JAVA_JUNIT_4 --outputFolder erc_20 --bbTargetUrl http://localhost:8081 --maxTime 10m

gitlab
java -jar evomaster.jar --blackBox true --bbSwaggerUrl file:///root/REST_Go/services/gitlab/gitlab-14.10.yml  --outputFormat JAVA_JUNIT_4 --outputFolder gitlab --bbTargetUrl http://10.0.24.1:81/api/v4 --maxTime 10m --header0 "Authorization: Bearer Bearer glpat-Dp_JE9mrhGcvxmpfoddL"

github
java -jar evomaster.jar --blackBox true --bbSwaggerUrl file:///root/REST_Go/services/github/github.json --outputFormat JAVA_JUNIT_4 --outputFolder github --bbTargetUrl https://api.github.com --maxTime 10m --header0 "Authorization: Bearer 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"