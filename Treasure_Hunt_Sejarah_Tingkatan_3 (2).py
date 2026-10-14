import tkinter as tk
from tkinter import simpledialog, messagebox
import random, math, json, os

# TREASURE HUNT: PENGEMBARAAN TOKOH PEJUANG TEMPATAN TINGKATAN 3
# Dibina menggunakan Tkinter (termasuk dalam kebanyakan pemasangan Python).

W, H = 1000, 650
BG = '#173b2b'
GOLD = '#ffd166'
WHITE = '#fff7dc'

QUIZZES = [
("Checkpoint 1: Tanah Melayu Menentang Campur Tangan", [
("Siapakah tokoh yang terkenal menentang British di Naning?", ["Dol Said", "Mat Salleh", "Rentap", "Tok Janggut"], 0),
("Naning terletak di negeri manakah pada hari ini?", ["Perak", "Melaka", "Pahang", "Sabah"], 1),
("Apakah sebab utama Dol Said menentang British?", ["Cukai dan dakwaan British terhadap Naning", "Larangan menangkap ikan", "Pembinaan lapangan terbang", "Perebutan lombong emas moden"], 0),
("Siapakah pemerintah yang menentang British di Pahang pada akhir abad ke-19?", ["Dato' Bahaman", "Rentap", "Antanom", "Dol Said"], 0),
("Apakah gelaran lain bagi Dato' Bahaman?", ["Orang Kaya Semantan", "Raja Laut", "Panglima Gunung", "Penghulu Naning"], 0),
("Siapakah tokoh yang menentang British di Perak bersama-sama pengikutnya?", ["Dato' Maharaja Lela", "Mat Salleh", "Haji Abdul Rahman Limbong", "Antanom"], 0),
("Apakah peristiwa penting yang berkaitan dengan Dato' Maharaja Lela?", ["Pembunuhan J.W.W. Birch", "Perang Naning pertama", "Kebangkitan Rundum", "Perang Kelantan"], 0),
("J.W.W. Birch ialah Residen British di negeri mana?", ["Perak", "Johor", "Kedah", "Terengganu"], 0),
("Apakah nilai yang ditunjukkan oleh tokoh-tokoh pejuang tempatan?", ["Keberanian mempertahankan tanah air", "Mementingkan diri", "Mengelak tanggungjawab", "Menolak semua ilmu"], 0),
("Apakah antara sebab penentangan masyarakat tempatan terhadap British?", ["Campur tangan dalam pentadbiran dan adat tempatan", "Pengenalan internet", "Pembukaan universiti", "Pembinaan lebuh raya moden"], 0),
]),
("Checkpoint 2: Pahlawan Pahang dan Kelantan", [
("Siapakah tokoh yang menentang British di Kelantan pada tahun 1915?", ["Tok Janggut", "Dol Said", "Rentap", "Mat Salleh"], 0),
("Apakah nama sebenar Tok Janggut?", ["Haji Mat Hassan bin Munas", "Mat Salleh", "Rentap anak Libau", "Awang Nong"], 0),
("Penentangan Tok Janggut berlaku di daerah manakah?", ["Pasir Puteh", "Kuala Lipis", "Naning", "Keningau"], 0),
("Antara berikut, apakah faktor penentangan Tok Janggut?", ["Pengenaan cukai dan isu pentadbiran British", "Pelarangan permainan video", "Pembinaan landasan angkasa", "Kekurangan kapal terbang"], 0),
("Siapakah tokoh yang turut dikenali sebagai Haji Abdul Rahman Limbong?", ["Tokoh penentangan di Terengganu", "Residen British di Perak", "Pemerintah Naning", "Pemimpin di Sabah"], 0),
("Penentangan Haji Abdul Rahman Limbong berlaku di negeri mana?", ["Terengganu", "Perlis", "Melaka", "Sarawak"], 0),
("Apakah yang ditentang oleh Haji Abdul Rahman Limbong?", ["Peraturan tanah yang membebankan rakyat", "Penggunaan perahu", "Perdagangan rempah", "Pembelajaran membaca"], 0),
("Dato' Bahaman menentang British di kawasan mana?", ["Pahang", "Kelantan", "Sabah", "Melaka"], 0),
("Siapakah antara pembesar yang bersama Dato' Bahaman dalam penentangan di Pahang?", ["Mat Kilau", "J.W.W. Birch", "James Brooke", "Hugh Clifford sahaja"], 0),
("Apakah pengajaran daripada perjuangan Tok Janggut?", ["Mempertahankan hak dan maruah masyarakat", "Mengabaikan masyarakat", "Menyerahkan semua keputusan tanpa bantahan", "Melupakan sejarah"], 0),
]),
("Checkpoint 3: Pejuang Sarawak dan Sabah", [
("Siapakah tokoh Iban yang menentang pemerintahan James Brooke?", ["Rentap", "Dol Said", "Tok Janggut", "Dato' Maharaja Lela"], 0),
("Apakah gelaran Rentap yang terkenal?", ["Raja Darat", "Raja Beruk", "Panglima Laut", "Orang Kaya Semantan"], 0),
("Rentap menentang pemerintahan keluarga Brooke di negeri mana?", ["Sarawak", "Perak", "Pahang", "Kelantan"], 0),
("Siapakah tokoh yang menentang Syarikat Borneo Utara British di Sabah?", ["Mat Salleh", "Dol Said", "Tok Janggut", "Haji Abdul Rahman Limbong"], 0),
("Penentangan Mat Salleh berlaku di wilayah yang kini dikenali sebagai negeri mana?", ["Sabah", "Johor", "Melaka", "Perak"], 0),
("Apakah antara sebab Mat Salleh menentang pentadbiran syarikat British?", ["Cukai dan campur tangan pentadbiran", "Larangan menggunakan telefon pintar", "Pertandingan sukan", "Pembinaan pusat membeli-belah"], 0),
("Siapakah pemimpin Murut yang mengetuai Kebangkitan Rundum pada 1915?", ["Antanom", "Rentap", "Mat Kilau", "Dol Said"], 0),
("Kebangkitan Rundum berlaku di kawasan mana?", ["Sabah", "Naning", "Perak", "Pahang"], 0),
("Apakah antara punca Kebangkitan Rundum?", ["Peraturan dan cukai yang membebankan masyarakat Murut", "Perebutan takhta di Melaka", "Larangan membina kapal terbang", "Kekurangan sekolah digital"], 0),
("Apakah persamaan perjuangan Rentap, Mat Salleh dan Antanom?", ["Menentang kuasa luar yang mengganggu kehidupan tempatan", "Menjadi Residen British", "Memimpin Naning", "Membina empayar Rom"], 0),
]),
("Checkpoint 4: Strategi dan Semangat Perjuangan", [
("Mengapakah sesetengah pejuang menggunakan kubu dalam perjuangan?", ["Untuk mempertahankan kawasan dan menghalang serangan", "Untuk menyimpan telefon", "Untuk mengadakan pilihan raya moden", "Untuk membina lapangan terbang"], 0),
("Apakah kelebihan pengetahuan tentang bentuk muka bumi kepada pejuang tempatan?", ["Membantu memilih laluan dan strategi", "Menghapuskan semua cukai secara automatik", "Menjadikan senjata moden", "Menghentikan masa"], 0),
("Mengapakah perpaduan penting dalam perjuangan?", ["Menguatkan kerjasama dan semangat", "Melemahkan semua pihak", "Mengelakkan komunikasi", "Memecah-belahkan masyarakat"], 0),
("Apakah kelemahan yang sering dihadapi pejuang tempatan berbanding kuasa British?", ["Kekurangan senjata moden dan sumber", "Terlalu banyak kapal angkasa", "Tiada pengetahuan tentang kawasan", "Mempunyai tentera yang jauh lebih besar"], 0),
("Apakah cara yang baik untuk mengkaji perjuangan tokoh tempatan?", ["Merujuk sumber sejarah yang boleh dipercayai", "Mereka-reka semua fakta", "Mengabaikan tarikh dan tempat", "Bergantung pada khabar angin sahaja"], 0),
("Apakah maksud kedaulatan dalam konteks sejarah?", ["Kuasa untuk mentadbir tanpa dikuasai pihak luar", "Sistem permainan", "Peraturan sekolah sahaja", "Perdagangan tanpa mata wang"], 0),
("Mengapakah British memperkenalkan sistem cukai di beberapa kawasan?", ["Untuk mengukuhkan pentadbiran dan hasil mereka", "Untuk memberi semua tanah percuma", "Untuk menghentikan perdagangan dunia", "Untuk membina taman tema"], 0),
("Apakah kesan campur tangan kuasa asing terhadap pembesar tempatan?", ["Kuasa dan pengaruh mereka boleh terjejas", "Semua menjadi pemerintah British", "Tiada perubahan langsung di mana-mana", "Semua negeri terus merdeka"], 0),
("Apakah sikap yang patut dicontohi daripada pejuang tempatan?", ["Berani, berprinsip dan cinta akan negara", "Mudah berputus asa", "Tidak menghormati masyarakat", "Menolak kerjasama"], 0),
("Mengapakah kita perlu mempelajari sejarah perjuangan tempatan?", ["Menghargai pengorbanan dan membina jati diri", "Supaya lupa asal usul", "Untuk mengulang kesilapan tanpa belajar", "Untuk menghapuskan semua warisan"], 0),
]),
("Checkpoint 5: Misi Peti Harta Karun", [
("Siapakah tokoh yang dikaitkan dengan penentangan di Naning?", ["Dol Said", "Antanom", "Mat Salleh", "Rentap"], 0),
("Siapakah tokoh yang dikaitkan dengan pembunuhan J.W.W. Birch dalam penentangan Perak?", ["Dato' Maharaja Lela", "Tok Janggut", "Antanom", "Rentap"], 0),
("Tok Janggut menentang British di Kelantan pada tahun berapa?", ["1915", "1831", "1840", "1948"], 0),
("Siapakah pemimpin yang menentang James Brooke di Sarawak?", ["Rentap", "Dol Said", "Tok Janggut", "Mat Kilau"], 0),
("Siapakah pemimpin Kebangkitan Rundum?", ["Antanom", "Dato' Bahaman", "Mat Salleh", "Dol Said"], 0),
("Mat Salleh menentang kuasa kolonial di mana?", ["Sabah", "Perak", "Melaka", "Terengganu"], 0),
("Apakah faktor umum yang mencetuskan banyak penentangan tempatan?", ["Cukai, campur tangan dan kehilangan kuasa", "Penggunaan komputer", "Pertandingan bola sepak", "Pembinaan pawagam"], 0),
("Apakah yang patut dilakukan apabila mendapat maklumat sejarah daripada internet?", ["Semak dengan sumber yang dipercayai", "Terus percaya semua maklumat", "Padam semua sumber", "Tukar fakta sesuka hati"], 0),
("Apakah maksud patriotisme?", ["Perasaan cinta dan setia kepada negara", "Sikap tidak peduli", "Keinginan melupakan negara", "Persaingan permainan semata-mata"], 0),
("Apakah ganjaran utama apabila kita memahami sejarah perjuangan tempatan?", ["Menghargai warisan dan semangat kebangsaan", "Mendapat kuasa ajaib", "Mengubah sejarah sebenar", "Menghapuskan semua cabaran"], 0),
]),
]

class TreasureGame:
    def __init__(self, root):
        self.root = root
        self.root.title('Treasure Hunt: Tokoh Pejuang Tempatan')
        self.root.geometry(f'{W}x{H}')
        self.root.resizable(False, False)
        self.name = simpledialog.askstring('Pengembara baharu', 'Masukkan nama pemain:', parent=root) or 'Pengembara'
        self.score = 0
        self.coins = 0
        self.cp = 0
        self.q_index = 0
        self.answers = 0
        self.x = 180
        self.y = 430
        self.lane = 1
        self.step = 0
        self.running = True
        self.finished = False
        self.score_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ranking_treasure_hunt.json')
        try:
            with open(self.score_file, 'r', encoding='utf-8') as f:
                self.leaderboard = json.load(f)
        except (OSError, ValueError):
            self.leaderboard = []
        self.canvas = tk.Canvas(root, width=W, height=H, bg=BG, highlightthickness=0)
        self.canvas.pack()
        self.canvas.bind_all('<Left>', lambda e: self.move_lane(-1))
        self.canvas.bind_all('<Right>', lambda e: self.move_lane(1))
        self.canvas.bind_all('<Up>', lambda e: self.jump())
        self.canvas.bind_all('<space>', lambda e: self.jump())
        self.draw_scene()
        self.animate()

    def draw_scene(self):
        c = self.canvas
        c.delete('all')
        # Sky and distant jungle
        c.create_rectangle(0, 0, W, H, fill='#193c32', outline='')
        c.create_oval(760, 35, 850, 125, fill='#ffd166', outline='')
        for i in range(14):
            xx = (i * 91 - self.step * 2) % (W + 100) - 40
            hh = 100 + (i % 4) * 22
            c.create_polygon(xx-65, 360, xx, 190 + (i%3)*18, xx+70, 360, fill=['#24543a','#2b6240','#1d4a35'][i%3], outline='')
            c.create_rectangle(xx-5, 330, xx+7, 410, fill='#4b3927', outline='')
        # path perspective
        c.create_polygon(310, H, 690, H, 570, 285, 430, 285, fill='#a98250', outline='#e7c78d', width=3)
        c.create_polygon(0, H, 310, H, 430, 285, 0, 285, fill='#28563b', outline='')
        c.create_polygon(690, H, W, H, W, 285, 570, 285, fill='#28563b', outline='')
        # path markings
        for i in range(8):
            yy = (300 + i*54 + self.step*5) % 560
            if yy > 290:
                half = (yy-285)*0.38
                c.create_line(500-half, yy, 500+half, yy, fill='#c9a36b', width=2)
        # ruins and vines
        c.create_rectangle(65, 235, 105, 360, fill='#82765b', outline='#d0bd91', width=3)
        c.create_rectangle(35, 225, 135, 245, fill='#a99a75', outline='#d0bd91', width=2)
        c.create_rectangle(865, 250, 905, 365, fill='#82765b', outline='#d0bd91', width=3)
        c.create_rectangle(835, 240, 935, 260, fill='#a99a75', outline='#d0bd91', width=2)
        # HUD
        c.create_rectangle(18, 16, 430, 108, fill='#10251f', outline=GOLD, width=2)
        c.create_text(35, 32, anchor='w', text='TREASURE HUNT  •  ZAMAN DAHULU', fill=GOLD, font=('Georgia', 15, 'bold'))
        c.create_text(35, 59, anchor='w', text=f'Pemain: {self.name}   Markah: {self.score}   Syiling: {self.coins}', fill=WHITE, font=('Arial', 12, 'bold'))
        c.create_text(35, 84, anchor='w', text=f'Checkpoint {min(self.cp+1,5)}/5   •   Soalan {min(self.q_index+1,10)}/10', fill='#d4e6cf', font=('Arial', 11))
        # checkpoints on trail
        for i in range(5):
            xx = 440 + i*30
            col = GOLD if i < self.cp else '#6b765e'
            c.create_oval(xx, 135, xx+20, 155, fill=col, outline=WHITE, width=1)
            c.create_text(xx+10, 145, text=str(i+1), fill='#243326', font=('Arial', 9, 'bold'))
        # player character, bobbing while running
        bob = int(5*math.sin(self.step/2))
        px = [435, 500, 565][self.lane]
        py = self.y + bob
        c.create_oval(px-26, py+28, px+26, py+40, fill='#14261f', outline='')
        c.create_rectangle(px-17, py-3, px+17, py+27, fill='#9b4e2e', outline='#f0c18a', width=2)
        c.create_oval(px-16, py-34, px+16, py-3, fill='#d8a16f', outline='#f0c18a', width=2)
        c.create_arc(px-17, py-39, px+17, py-5, start=0, extent=180, fill='#3a251b', outline='#3a251b', width=5)
        c.create_line(px-10, py+5, px-26, py+18, fill='#d8a16f', width=6)
        c.create_line(px+10, py+5, px+26, py+18, fill='#d8a16f', width=6)
        c.create_line(px-8, py+26, px-14, py+42, fill='#392c26', width=7)
        c.create_line(px+8, py+26, px+14, py+42, fill='#392c26', width=7)
        # chest / destination
        c.create_rectangle(750, 410, 810, 455, fill='#8b4c25', outline=GOLD, width=3)
        c.create_rectangle(746, 402, 814, 418, fill='#c58a36', outline=GOLD, width=2)
        c.create_rectangle(775, 415, 785, 432, fill=GOLD, outline='')
        c.create_text(780, 475, text='PETI HARTA', fill=GOLD, font=('Georgia', 11, 'bold'))
        # controls footer
        c.create_rectangle(20, 570, 980, 630, fill='#10251f', outline='#c29b5d', width=2)
        c.create_text(500, 588, text='KAWALAN:  ← → Tukar lorong   •   ↑ / SPACE Lompat   •   Jawab kuiz untuk membuka laluan', fill=WHITE, font=('Arial', 12, 'bold'))
        c.create_text(500, 610, text='Misi: Kumpulkan ilmu, lepasi 5 checkpoint dan temui peti harta karun!', fill='#d7c79d', font=('Arial', 11))
        # progress glow
        c.create_rectangle(440, 166, 560, 174, fill='#384d3b', outline='')
        c.create_rectangle(440, 166, 440 + 120*(self.cp/5), 174, fill=GOLD, outline='')

    def move_lane(self, direction):
        if self.finished: return
        self.lane = max(0, min(2, self.lane + direction))
        self.coins += 1
        self.score += 2
        self.draw_scene()

    def jump(self):
        if self.finished: return
        self.score += 1
        self.draw_scene()
        self.canvas.create_text(500, 235, text='LOMPAT!', fill=GOLD, font=('Arial', 18, 'bold'))

    def animate(self):
        if not self.running: return
        self.step += 1
        if self.step % 12 == 0:
            self.coins += 1
            self.score += 1
        self.draw_scene()
        if self.step % 90 == 0 and not self.finished:
            self.show_checkpoint_quiz()
        self.root.after(90, self.animate)

    def show_checkpoint_quiz(self):
        if self.finished: return
        title, questions = QUIZZES[self.cp]
        self.running = False
        messagebox.showinfo('Checkpoint ditemui!', f'{title}\n\nJawab 10 soalan untuk membuka laluan seterusnya.\nMarkah semasa: {self.score}', parent=self.root)
        for i, (question, options, correct) in enumerate(questions):
            self.q_index = i
            self.draw_scene()
            answer = self.ask_question(title, i+1, question, options)
            if answer is None:
                answer = -1
            if answer == correct:
                self.score += 100
                self.coins += 5
                messagebox.showinfo('Jawapan tepat!', 'Hebat! +100 markah dan +5 syiling.', parent=self.root)
            else:
                correct_text = options[correct]
                messagebox.showinfo('Teruskan pengembaraan', f'Belum tepat. Jawapan yang betul: {correct_text}\nTeruskan belajar dan cuba lagi!', parent=self.root)
        self.cp += 1
        self.q_index = 0
        if self.cp >= len(QUIZZES):
            self.finish_game()
        else:
            messagebox.showinfo('Checkpoint selesai!', f'{title} selesai!\nCheckpoint seterusnya telah dibuka.', parent=self.root)
            self.running = True

    def ask_question(self, title, number, question, options):
        win = tk.Toplevel(self.root)
        win.title(f'{title} — Soalan {number}/10')
        win.configure(bg='#18382b')
        win.geometry('720x330')
        win.transient(self.root)
        win.grab_set()
        tk.Label(win, text=f'🗺️  {title}  |  SOALAN {number}/10', bg='#18382b', fg=GOLD, font=('Georgia', 15, 'bold'), wraplength=680).pack(pady=(18,10))
        tk.Label(win, text=question, bg='#18382b', fg=WHITE, font=('Arial', 14, 'bold'), wraplength=670, justify='center').pack(pady=8)
        choice = tk.IntVar(value=-1)
        for idx, option in enumerate(options):
            tk.Radiobutton(win, text=f'{chr(65+idx)}. {option}', variable=choice, value=idx, bg='#18382b', fg=WHITE, selectcolor='#315744', activebackground='#18382b', activeforeground=GOLD, font=('Arial', 12), anchor='w', padx=24).pack(fill='x', padx=90, pady=2)
        result = {'answer': None}
        def submit():
            if choice.get() < 0:
                messagebox.showwarning('Pilih jawapan', 'Sila pilih satu jawapan dahulu.', parent=win)
                return
            result['answer'] = choice.get()
            win.destroy()
        tk.Button(win, text='KUNCI JAWAPAN', command=submit, bg='#d89b32', fg='#1b2c21', font=('Arial', 12, 'bold'), relief='flat', padx=18, pady=7).pack(pady=12)
        self.root.wait_window(win)
        return result['answer']

    def finish_game(self):
        self.finished = True
        self.running = False
        self.leaderboard.append([self.name, self.score, self.coins])
        self.leaderboard.sort(key=lambda row: (row[1], row[2]), reverse=True)
        self.leaderboard = self.leaderboard[:10]
        try:
            with open(self.score_file, 'w', encoding='utf-8') as f:
                json.dump(self.leaderboard, f, ensure_ascii=False, indent=2)
        except OSError:
            pass
        self.canvas.delete('all')
        self.canvas.create_rectangle(0,0,W,H,fill='#142f25',outline='')
        self.canvas.create_text(W//2, 105, text='🏆 HARTA KARUN DITEMUI! 🏆', fill=GOLD, font=('Georgia', 30, 'bold'))
        self.canvas.create_text(W//2, 165, text='TAHNIAH, PENGEMBARA!', fill=WHITE, font=('Georgia', 22, 'bold'))
        self.canvas.create_text(W//2, 220, text=f'{self.name}  •  Markah: {self.score}  •  Syiling: {self.coins}', fill='#d6e7d4', font=('Arial', 17, 'bold'))
        self.canvas.create_text(W//2, 290, text='PAPAN RANKING', fill=GOLD, font=('Georgia', 20, 'bold'))
        for idx, row in enumerate(self.leaderboard[:5]):
            self.canvas.create_text(W//2, 330 + idx*31, text=f'{idx+1}. {row[0]}  —  {row[1]} mata  |  {row[2]} syiling', fill=WHITE if idx else GOLD, font=('Arial', 14, 'bold' if idx == 0 else 'normal'))
        self.canvas.create_text(W//2, 505, text='Kamu telah menamatkan 5 checkpoint dan menjawab 50 soalan Sejarah!', fill='#d6e7d4', font=('Arial', 13), width=850)
        btn = tk.Button(self.root, text='KELUAR GAME', command=self.root.destroy, bg='#d89b32', fg='#1b2c21', font=('Arial', 13, 'bold'), relief='flat', padx=20, pady=8)
        self.canvas.create_window(W//2, 570, window=btn)

if __name__ == '__main__':
    root = tk.Tk()
    app = TreasureGame(root)
    root.mainloop()
