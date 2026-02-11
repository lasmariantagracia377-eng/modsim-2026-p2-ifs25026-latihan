target_question = input()

if target_question == "q1":
    # Pada kusioner dari keseluruhan data, skala mana yang paling banyak dipilih oleh partisipan? sertakan jumlah dan persen
    # Contoh Jawaban: CS|500|70.1
    print("CS|500|70.1")

elif target_question == "q2":
    # Pada kusioner dari keseluruhan data, skala mana yang paling sedikit dipilih oleh partisipan? sertakan jumlah dan persen
    # Contoh Jawaban: TS|1|1.1
    print("STS|4|0.2")

elif target_question == "q3":
    # Pada kusioner dari pertanyaan Q1 sampai Q17, pertanyaan mana yang pilihan skala SS (Sangat Setuju) paling banyak? sertakan jumlah dan persen
    # Contoh Jawaban: Q2|30|34.4
    print("Q9|21|18.6")

elif target_question == "q4":
    # Pada kusioner dari pertanyaan Q1 sampai Q17, pertanyaan mana yang pilihan skala S (Setuju) paling banyak? sertakan jumlah dan persen
    # Contoh Jawaban: Q2|30|34.4
    print("Q16|75|66.4")

elif target_question == "q5":
    # Pada kusioner dari pertanyaan Q1 sampai Q17, pertanyaan mana yang pilihan skala CS (Cukup Setuju) paling banyak? sertakan jumlah dan persen
    # Contoh Jawaban: Q2|30|34.4
    print("Q2|36|31.9")

elif target_question == "q6":
    # Pada kusioner dari pertanyaan Q1 sampai Q17, pertanyaan mana yang pilihan skala CTS (Cukup Tidak Setuju) paling banyak? sertakan jumlah dan persen
    # Contoh Jawaban: Q2|30|34.4
    print("Q9|8|7.1")

elif target_question == "q7":
    # Pada kusioner dari pertanyaan Q1 sampai Q17, pertanyaan mana yang pilihan skala TS (Tidak Setuju) paling banyak? sertakan jumlah dan persen
    # Contoh Jawaban: Q2|30|34.4
    print("Q12|3|2.7")

elif target_question == "q8":
    # Pada kusioner dari pertanyaan Q1 sampai Q17, pertanyaan mana yang pilihan skala TS (Tidak Setuju) paling banyak? sertakan jumlah dan persen
    # Contoh Jawaban: Q2|30|34.4
    print("Q12|3|2.7")

elif target_question == "q9":
    # Pada kusioner dari pertanyaan Q1 sampai Q17, pertanyaan mana saja yang terdapat memilih skala STS (Sangat Tidak Setuju)? sertakan jumlah dan persen
    # Contoh Jawaban: Q1:0.1|Q2:0.2|Q3:0.1
    print("Q1:0.9|Q2:0.9|Q9:0.9|Q11:0.9")

elif target_question == "q10":
    # Jika skala skor untuk masing masing skala adalah 6, 5, 4, 3, 2, 1 untuk SS, S, CS, CTS, TS, STS
    # Berapa skor rata-rata keseluruhan pertanyaan?
    # Contoh Jawaban: 5.60
    print("4.80")

elif target_question == "q11":
    # Jika skala skor untuk masing masing skala adalah 6, 5, 4, 3, 2, 1 untuk SS, S, CS, CTS, TS, STS
    # Maka pada kusioner dari pertanyaan Q1 sampai Q17, pertanyaan mana yang memiliki skor rata-rata tertinggi?
    # Contoh Jawaban: Q1:5.60
    print("Q5:4.95")

elif target_question == "q12":
    # Jika skala skor untuk masing masing skala adalah 6, 5, 4, 3, 2, 1 untuk SS, S, CS, CTS, TS, STS
    # Maka pada kusioner dari pertanyaan Q1 sampai Q17, pertanyaan mana yang memiliki skor rata-rata terendah?
    # Contoh Jawaban: Q2:3.60
    print("Q12:4.59")

elif target_question == "q13":
    # Jika skala di kategorikan menjadi positif (SS dan S), netral (CS) dan negatif (CTS, TS dan STS)
    # Maka hitung jumlah responden dan persentase masing-masing kategori
    # Contoh Jawaban: positif=1000:80.1|netral=200:10.1|negatif=200:100.2
    print("positif=1396:72.7|netral=471:24.5|negatif=54:2.8")