import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict

# Create causative examples database
causative_data = {
    'Language': [],
    'Type': [],
    'Base_Form': [],
    'Causative_Form': [],
    'Translation': [],
    'Example_Sentence': []
}

# Korean Morphological Causatives
korean_morphological = [
    ('먹다', '먹이다', 'eat → feed', '-이', '엄마가 아이에게 밥을 먹였다'),
    ('앉다', '앉히다', 'sit → seat', '-히', '선생님이 학생을 의자에 앉혔다'),
    ('울다', '울리다', 'cry → make cry', '-리', '그가 아이를 울렸다'),
    ('신다', '신기다', 'wear → make wear', '-기', '엄마가 아이에게 신발을 신겼다'),
    ('자다', '재우다', 'sleep → put to sleep', '-우', '엄마가 아기를 재웠다'),
    ('솟다', '솟구다', 'rise → make rise', '-구', '물이 하늘로 솟구쳤다'),
    ('맞다', '맞추다', 'fit → adjust', '-추', '시간을 맞추었다')
]

# Malay Morphological Causatives
malay_morphological = [
    ('pakai', 'memakaikan', 'wear → make wear', 'meN-...-kan', 'Ibu memakaikan baju kepada adik'),
    ('tidur', 'menidurkan', 'sleep → put to sleep', 'meN-...-kan', 'Ali menidurkan anaknya di bilik'),
    ('duduk', 'mendudukkan', 'sit → seat', 'meN-...-kan', 'Guru mendudukkan murid di kerusi'),
    ('baca', 'membacakan', 'read → read to/for', 'meN-...-kan', 'Ayah membacakan cerita kepada anak'),
    ('tulis', 'menuliskan', 'write → write for', 'meN-...-kan', 'Setiausaha menuliskan minit mesyuarat'),
    ('satu', 'menyatukan', 'one → unite', 'meN-...-kan', 'Projek ini menyatukan data dari berbagai sumber'),
    ('dua', 'menduakan', 'two → betray/duplicate', 'meN-...-kan', 'Abu menduakan isterinya')
]

# Malay Lexical Causatives
malay_lexical = [
    ('mati', 'membunuh', 'die → kill', 'lexical', 'Pembunuh itu membunuh mangsa'),
    ('pecah', 'memecahkan', 'break → break (tr.)', 'lexical', 'Dia memecahkan kaca'),
    ('tumbuh', 'menumbuhkan', 'grow → make grow', 'lexical', 'Petani menumbuhkan sayuran')
]

# Malay Periphrastic Causatives
malay_periphrastic = [
    ('pergi', 'suruh pergi', 'go → make go', 'suruh', 'Dia suruh saya pergi'),
    ('makan', 'suruh makan', 'eat → make eat', 'suruh', 'Saya suruh dia makan'),
    ('menangis', 'buat menangis', 'cry → make cry', 'buat', 'Saya buat dia menangis')
]

# Korean Periphrastic Causatives
korean_periphrastic = [
    ('가다', '가게 하다', 'go → make go', '-게 하다', '나는 그를 가게 했다'),
    ('먹다', '먹게 하다', 'eat → make eat', '-게 하다', '나는 동생에게 밥을 먹게 했다'),
    ('자다', '자게 하다', 'sleep → make sleep', '-게 하다', '나는 아이를 자게 했다')
]

# Compile all data
def add_to_database(data_list, language, type_name):
    for item in data_list:
        causative_data['Language'].append(language)
        causative_data['Type'].append(type_name)
        causative_data['Base_Form'].append(item[0])
        causative_data['Causative_Form'].append(item[1])
        causative_data['Translation'].append(item[2])
        if len(item) > 4:
            causative_data['Example_Sentence'].append(item[4])
        else:
            causative_data['Example_Sentence'].append('')

# Add all data
add_to_database(korean_morphological, 'Korean', 'Morphological')
add_to_database(malay_morphological, 'Malay', 'Morphological')
add_to_database(malay_lexical, 'Malay', 'Lexical')
add_to_database(malay_periphrastic, 'Malay', 'Periphrastic')
add_to_database(korean_periphrastic, 'Korean', 'Periphrastic')

# Create DataFrame
df = pd.DataFrame(causative_data)

# Save to CSV
df.to_csv('C:\\Users\\User\\Documents\\L2-Ongoing\\May task\\N56501\\data\\causative_examples.csv', index=False, encoding='utf-8-sig')

print("Data collection completed. Total examples:", len(df))
print("\nBreakdown by language and type:")
print(df.groupby(['Language', 'Type']).size())
