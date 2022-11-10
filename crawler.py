from bs4 import BeautifulSoup
from html_table_parser import parser_functions
import requests
import pandas as pd
import os 
import csv

def crawl(url):


    table=pd.read_html(url,
    attrs={'class':'table table-striped table-responsive  table-condensed no-space table-bordered'})[0] #인코딩 옵션 추가 없을 때 한글 깨짐 현상
    df = pd.DataFrame(table).drop_duplicates()
    #df.dropna(axis=1,how='any',inplace=True) 정상 데이터까지 삭제하는 오류. 임시 삭제

    return df

def will_save():
    error_count=0

    while True:
        if error_count==0:
            save=input('저장하시겠습니까? Y/N \n')
            if save.lower() in ['y','n']:
                break

        error_count+=1
        
        if error_count>0:
            save=input('저장하시겠습니까? "Y/N" 중 하나를 골라주세요 \n')

            if save.lower() in ['y','n']:
                break
    
    is_save= True if save.lower()=='y' else False

    return is_save

if __name__ == '__main__':

    welcome='''
    고려대학교 통계학과 동아리 PAINS
    -------------------------------------------------------------
    스탯티즈 자료 자동 추출 프로그램 V.2
    -------------------------------------------------------------
                        주의사항

    1. 오류 발생시 V3 등 컴뷰터 백신 프로그램을 일시정지 해보세요

    2. 오류 발생시 종료 후 다시 실행 해보세요.

    기타 문의 및 건의사항은 
    
    painsports1905@gmail.com 으로 보내주세요!
    
    * 주의: 팀 기록 크롤링의 경우 빈 데이터 열이 
      추가로 크롤링 되는 오류가 있습니다.
      빠른 시일 내에 수정하겠습니다.
    
    '''

    prompt="""
    
    원하는 기능을 입력해주세요
    
    1. 기록 크롤링
    2. 종료
    
    숫자를 입력해주세요:
    
    """

    while True:

        print(welcome)
    
        prompt_key=input(prompt)

        if prompt_key not in ['1','2']:

            print('잘못된 입력입니다!')

            continue

        elif prompt_key == '1':

            while True:

                url=input('\n 크롤링하고자 하는 스탯티즈 페이지 URL을 입력해주세요: ')

                try:
                    table=crawl(url)
                    break
                except:
                    print('올바른 입력이 아닙니다. 다시 시도해주세요')

            print('\n',table)

            is_save=will_save()

            if is_save:
                while True:
                    name=input('\n 파일명을 설정해주세요: ')
                    try:
                        make_dirs='files/'

                        os.makedirs(make_dirs,exist_ok=True)
                        full_path=os.path.join('./files',name+'.csv')

                        table.to_csv(full_path,index=False,encoding='euc-kr') 
                        print('\n {} 경로에 저장 성공!'.format(os.path.abspath(full_path)))
                        break
                    except:
                        print('\n 저장에 실패했습니다.')    
     
        else:
            break

