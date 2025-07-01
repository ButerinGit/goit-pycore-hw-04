def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            total = 0
            count = 0

            for line in lines:
                parts = line.strip().split(',')
                    
                if len(parts) == 2 and parts[1].isdigit():
                    total += int(parts[1])
                    count += 1
            
            
            if count == 0 or total == 0:
                return (0,0)

            avg = total/count
            return (total , avg)

    except FileNotFoundError:
        print('файл не знайдено')
        return (0,0)


g = total_salary('hm1/hm1.txt')

print(g)