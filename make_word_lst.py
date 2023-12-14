import json

word_pairs = [
    ('冬休み', '春休み'),
    ('副業', 'アルバイト'),
    ('風呂掃除', '食器洗い'),
    ('twitter', 'Line'),
    ('水族館', '動物園'),
    ('ドラえもん', 'ドラミちゃん'),
    ('ファミレス', 'カフェ'),
    ('アルバイト面接', '就活'),
    ('お年玉', '誕生日プレゼント'),
    ('ガラケー', '固定電話'),
    ('太陽', '月'),
    ('マフラー', '手袋'),
    ('エレベーター', 'エスカレーター'),
    ('コンビニ', 'スーパー'),
    ('海', 'プール'),
    ('年末', '年始'),
    ('コンタクトレンズ', 'メガネ'),
    ('セロテープ', 'ガムテープ'),
    ('東京タワー', 'スカイツリー'),
    ('コップ', 'グラス'),
    ('カブトムシ', 'クワガタ'),
    ('飛行機', '新幹線'),
    ('カレー', 'シチュー'),
    ('はさみ', 'カッター'),
    ('テニス', '卓球'),
    ('スケート', 'スキー'),
    ('りす', 'ハムスター'),
    ('ぞう', 'きりん'),
    ('タクシー', 'バス'),
    ('セミ', '鈴虫'),
    ('扇風機', 'クーラー'),
    ('ディズニーランド', 'USJ'),
    ('浮き輪', '水中メガネ'),
    ('洗濯機', '食洗機'),
    ('ブランコ', 'シーソー'),
    ('水中メガネ', '浮き輪'),
    ('サッカー', 'ラグビー'),
    ('１億円', '１０００万' ),
    ('炎', '赤'),
    ('時間', 'お金'),
    ('痴漢', '鬼ごっこ'),
    ('赤ちゃん', 'ハムスター'),
    ('ウォータースライダー', '流しそうめん'),
    ('塩', '砂糖'),
    ('白菜', 'キャベツ'),
    ('チョコレート', 'キャラメル'),
    ('コーヒー', '紅茶'),
    ('浮気', '不倫'),
    ('片思い', '失恋'),
    ('ガスト', 'サイゼリア'),
    ('すき屋', '吉野家'),
    ('セブンイレブン', 'ファミリーマート'),
    ('楽天市場', 'Amazon'),
    ('東京タワー', 'スカイツリー'),
    ('ハサミ', 'カッター'),

    ("野球", "卓球"),
    ("鮭", "鯛"),
    ("コンタクト", "サングラス"),
    ("仏像", "銅像"),
    ("泥棒", "スパイ"),
    ("喧嘩", "いたずら"),
    ("日本語", "漢字"),
    ("漬物", "白菜"),
    ("シャンプー", "洗剤"),
    ("しおり", "アルバム"),
    ("ヘリコプター", "軽トラック"),
    ("市役所", "郵便局"),
    ("ヨット", "パラシュート"),
    ("下水道", "トイレ"),
    ("懐中電灯", "豆電球"),
    ("サイコロ", "ルービックキューブ"),
    ("三つ編み", "蝶々結び"),
    ("アイマスク", "眼帯"),
    ("ビンタ", "ツッコミ"),
    ("近道", "裏口"),
    ("感想", "推理"),
    ("ロッテリア", "モスバーガー"),
    ("隕石", "UFO"),
    ("サボテン", "サソリ"),
    ("裏技", "不具合"),
    ("暗闇", "停電"),
    ("ニコチン", "カフェイン"),
    ("喫茶店", "茶店"),
    ("メイド", "コスプレ"),
    ("サボテン", "サソリ"),
    ("迷惑メール", "チラシ"),
    ("貧乏ゆすり", "バイブレーション"),
    ("幸運", "大吉"),
    ("ドローン", "タケコプター"),
    ("通り魔", "暗殺者"),
    ("進路", "線路"),
    ("ギプス", "コルセット"),
    ("人工呼吸", "口移し"),
    ("妄想", "空想"),
    ("スパルタ", "禁欲"),
    ("タオル", "ハチマキ"),
    ("しょうじ", "ふすま"),
    ("あんまん", "だいふく"),
    ("控え室", "更衣室"),
    ("講演", "説教"),
    ("スカウト", "ナンパ"),
    ("お賽銭", "募金"),
    ("村長", "生徒会長"),
    ("ブログ", "ツイッター"),
    ("故障", "エラー"),
    ("100万円", "1億円"),
    ("太陽", "ハゲ頭"),
    ("4", "6"),
    ("2000円札", "小判"),
    ("炎", "赤"),
    ("証明写真", "自撮り"),
    ("ゴリラ", "マッチョ"),
    ("人形", "こけし"),
    ("のぞき", "カンニング"),
    ("変態", "天才"),
    ("宇宙船", "ガンダム"),
    ("桃太郎", "鬼滅の刃"),
    ("セーラームーン", "おジャ魔女ドレミ"),
    ("妖怪ウォッチ", "デジモン"),
    ("ボボボーボ・ボーボボ", "でんじゃらすじーさん"),
    ("呪術廻戦", "BLEACH"),
    ("遊戯王", "ヴァンガード"),
    ("ドラえもん", "笑うせえるすまん"),
    ("ちはやふる", "ヒカルの碁"),
    
    ("ヒゲ", "すね毛"),
    ("ハエ", "ゴキブリ"),
    ("落石", "落雷"),
    ("果たし状", "ラブレター"),
    ("スプーン", "しゃもじ"),
    ("化粧", "歯磨き"),
    ("ルーレット", "サイコロ"),
    ("コーンフレーク", "カロリーメイト"),
    ("テニス", "卓球"),
    ("エステ", "美容整形"),
    ("映画館", "プラネタリウム"),
    ("教科書", "ノート"),
    ("にんにく", "納豆"),
    ("ディズニー映画", "ジブリ映画"),
    ("椅子取りゲーム", "ハンカチ落とし"),
    ("子猫", "年下の恋人"),
    ("チューバ", "コントラバス"),
    ("味噌ラーメン", "かけ蕎麦"),
    ("サッカー", "バレーボール"),
    ("餅つき", "お月見"),
    ("ネイル", "塗り絵"),
    ("吊り橋", "トンネル"),
    ("サングラス", "ゴーグル"),
    ("家族", "親友"),
    ("玉ねぎ", "にんじん"),
    ("電車", "バス"),
    ("社長", "政治家"),
    ("カメムシ", "カエル"),
    ("スキンヘッド", "電球"),
    ("ペンギン", "しろくま"),
    ("ピアノの教師", "英語の教師"),
    ("ワニワニパニック", "黒髭危機一発"),
    ("紙芝居", "人形劇"),
    ("チワワ", "柴犬"),
    ("豆乳", "野菜ジュース"),
    ("運", "便意"),
    ("空腹", "徹夜"),
    ("ゴルフ", "野球"),
    ("日本", "宇宙"),
    ("ホッチキス", "カッター"),
    ("エステ", "ヨガ"),
    ("耳栓", "アイマスク"),
    ("親子丼", "のり弁当"),
    ("嬉し泣き", "悲し泣き"),
    ("アフロ", "金髪"),
    ("ナポリタン", "とろろ蕎麦"),
    ("坊主", "ブリーチ"),
    ("レゴ", "ビーズ"),
    ("農業", "建設業"),
    ("笑いを見る", "スポーツを見る"),
    ("水風船", "水鉄砲"),
    ("神社", "お墓"),
    ("居酒屋", "バー"),
    ("嘘つき", "ぶりっ子"),
    ("ファーストキス", "初恋"),
    ("眉毛カット", "マツエク"),
    ("バリカン", "鼻毛カッター"),
    ("アミノ酸", "ミネラル"),
    ("映画", "劇場"),
    ("ケーキ", "パフェ"),
    ("キャビア", "フカヒレ"),
    ("牧場", "果樹園"),
    ("整形", "タトゥー"),
    ("ゴルフ", "ゲートボール"),
    ("アパレル", "マスコミ"),
    ("アイス", "かき氷"),
    ("ポケモンカード", "遊戯王カード"),
    ("世界一周", "宇宙旅行")

]

# 重複を取り除くためにセットに変換し、再びリストに戻す
unique_word_pairs = list(set(word_pairs))

print(len(word_pairs))
print(len(unique_word_pairs))

# JSONファイルに保存
with open('word_pairs.json', 'w', encoding='utf-8') as f:
    json.dump(unique_word_pairs, f, ensure_ascii=False, indent=4)