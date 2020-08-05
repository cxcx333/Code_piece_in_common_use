headers_origin, headers = ''':authority: getquicker.net
:method: GET
:path: /Share?code=ef3d0486-ea1c-4b77-2afa-08d65d1c0fb9
:scheme: https
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: en-US,en;q=0.9
cache-control: max-age=0
cookie: Hm_lvt_7bab827f502b0ce36fc1dce2b3656412=1591255117; .AspNetCore.Identity.Application=CfDJ8MeYFQPza-1Jg5BJ_dk45RPuI2CzyKz7wyspco50BLu2_AzURawmEsKpIE47cDYKLxPNseZv56nrQvRjZRSC1eX-3QXBAjGmYioewOwRDPzQ6RWK9tT1stdk4LbdHL0ALuOcGP2B2M2-Ahw9eFxVCR-pFv3Y56Squnr05EVxu8xBD7E-b-wjoiOuKFNzG6S-4jRxULGRXarRM3qYt_3dQR2eG1iYagv28vG4hkse2_rsfwtX9X452r44rYxMjagLHVlTdEy8vhnxIi2rmskaIUIHUn1vUTc9S3zHnq2FdcCRmhe-e3ZU-PJVHhYwHn-oj-UWvael4uyv4Z7kMkccvk3LlI_TJHVHHXwfTdc9Y6BN-8Xv0SSPGVvFLAxeB5yPhcB9M2hcf7OWDIiw_LPuFNpxSMing6_wRIn-Xj9NV8dQAIx4xp0GR8REShgzkx23KSEGBkvvZssKVKBpF8-pZHc0n1iTlDCU-E-m_XVNSDuGS4BRN4qQAfe_5u5Et3ylxhaB6qIKfwyAAH5d6f3SHtZE9MDgEX825DPEWXNkOPrD-TLl1GkUAIReC9E7owsXKkUF9nc-TAfOxnBzrsh8O6N5hoqDcsmpJ0H99UeV-ZWu
dnt: 1
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: none
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.142 Safari/537.36''', {}

for r in headers_origin.splitlines():
    headers[r.split(": ")[0]] = r.split(": ")[1].replace("\n", "")
