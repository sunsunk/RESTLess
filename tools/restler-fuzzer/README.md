Usage:
dotnet /root/REST_Go/restler-fuzzer/restler_bin/restler/Restler.dll compile --api_spec /root/REST_Go/services/languagetool/languagetool1.1.2.json

 dotnet /root/REST_Go/restler-fuzzer/restler_bin/restler/Restler.dll fuzz-lean --grammar_file ./Compile/grammar.py --dictionary_file ./Compile/dict.json --settings ./Compile/engine_settings.json --no_ssl

 gitlab:
 dotnet /root/REST_Go/restler-fuzzer/restler_bin/restler/Restler.dll fuzz-lean --grammar_file ./Compile/grammar.py --dictionary_file ./Compile/dict.json --settings ./Compile/engine_settings.json --token_refresh_command "python3 /root/REST_Go/restler-fuzzer/auth/gitlab_auth.py" --token_refresh_interval 720 --no_ssl