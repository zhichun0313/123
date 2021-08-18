d = dict() # 空字典

s = '''
1. 新增 k,v
2. 修改 v 
3. 刪除
4. 查詢
5. 列出所有資料
6. 刪除所有資料
9. 結束
請選擇:
'''

while True:
    menu = input(s)
    if menu == '1':
        print('------- 新增資料 -------')
        k = input('輸入郵遞區號: ')
        if k in d:
            print('新增失敗 , key 已存在:', k)
        else:
            v = input('輸入地區名稱: ')
            d[k] = v    # 新增資料
            print('新增成功')
    elif menu=='2':
         print('------- 修改資料 -------')
         k = input('輸入郵遞區號: ')
         if k in d:
            v = d[k]
            print('v', v)            
            v = input('輸入新地區名稱: ')
            d[k] = v    # 新增資料
            print('修改成功')            
         else:
            print('修改失敗，查無資料')
    elif menu == '3':
        print('------- 刪除資料 -------')
        k = input('輸入郵遞區號: ')
        if k in d:
            print('刪除成功')
            print(d[k])
            del d[k]
        else:
            print('刪除失敗，查無資料')
    elif menu == '4':
        print('------- 查詢資料 -------')
        k = input('輸入郵遞區號: ')
        if k in d:
            print(d[k])
        else:
            print('查無資料')
        
    elif menu == '5':
        print('------- 列出所有資料 -------')
        for k,v in d.items():
            print(k, v)
    elif menu=='6':
        d.clear() 
        print('----- 刪除所有資料 -----')
          
    elif menu == '9':
        break
print('結束')