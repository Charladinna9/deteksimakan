-- Jalankan sekali pada database mbg_db jika tabel tkpi belum memiliki kolom klasifikasi pangan.

ALTER TABLE tkpi
    ADD COLUMN kelompok_pangan VARCHAR(50) NULL AFTER nama_makanan,
    ADD COLUMN keterangan_gizi VARCHAR(255) NULL AFTER kelompok_pangan;

UPDATE tkpi
SET 
    kelompok_pangan = CASE LOWER(nama_makanan)

        WHEN 'nasi' THEN 'Karbohidrat'
        WHEN 'kentang' THEN 'Karbohidrat'
        WHEN 'mie' THEN 'Karbohidrat'
        WHEN 'roti' THEN 'Karbohidrat'
        WHEN 'jagung' THEN 'Karbohidrat'

        WHEN 'ayam' THEN 'Protein hewani'
        WHEN 'bakso' THEN 'Protein hewani'
        WHEN 'telur' THEN 'Protein hewani'

        WHEN 'tempe' THEN 'Protein nabati'
        WHEN 'tahu' THEN 'Protein nabati'
        WHEN 'kacang' THEN 'Protein nabati'
        WHEN 'kacang panjang' THEN 'Protein nabati'

        WHEN 'susu' THEN 'Kalsium & protein'
        WHEN 'keju' THEN 'Kalsium & protein'

        WHEN 'apel' THEN 'Buah'
        WHEN 'salak' THEN 'Buah'
        WHEN 'buah naga' THEN 'Buah'
        WHEN 'melon' THEN 'Buah'
        WHEN 'semangka' THEN 'Buah'
        WHEN 'pisang' THEN 'Buah'
        WHEN 'kelengkeng' THEN 'Buah'
        WHEN 'anggur' THEN 'Buah'
        WHEN 'jeruk' THEN 'Buah'

        WHEN 'tomat' THEN 'Sayuran'
        WHEN 'kol' THEN 'Sayuran'
        WHEN 'sawi' THEN 'Sayuran'
        WHEN 'timun' THEN 'Sayuran'
        WHEN 'selada' THEN 'Sayuran'
        WHEN 'wortel' THEN 'Sayuran'

        ELSE 'Lainnya'

    END,

    keterangan_gizi = CASE LOWER(nama_makanan)

        WHEN 'nasi' THEN 'Sumber energi utama dari karbohidrat.'
        WHEN 'kentang' THEN 'Sumber karbohidrat dan kalium.'
        WHEN 'mie' THEN 'Sumber karbohidrat untuk energi.'
        WHEN 'roti' THEN 'Sumber karbohidrat praktis.'
        WHEN 'jagung' THEN 'Sumber karbohidrat, energi, dan serat.'

        WHEN 'ayam' THEN 'Sumber protein hewani untuk pertumbuhan.'
        WHEN 'bakso' THEN 'Sumber protein hewani.'
        WHEN 'telur' THEN 'Sumber protein hewani dan zat gizi mikro.'

        WHEN 'tempe' THEN 'Sumber protein nabati dan serat.'
        WHEN 'tahu' THEN 'Sumber protein nabati.'
        WHEN 'kacang' THEN 'Sumber protein nabati dan lemak baik.'
        WHEN 'kacang panjang' THEN 'Sumber protein nabati, serat, vitamin, dan mineral.'

        WHEN 'susu' THEN 'Sumber kalsium dan protein.'
        WHEN 'keju' THEN 'Sumber kalsium dan protein serta lemak.'

        WHEN 'apel' THEN 'Sumber vitamin, mineral, dan serat.'
        WHEN 'salak' THEN 'Sumber karbohidrat, vitamin, dan serat.'
        WHEN 'buah naga' THEN 'Sumber vitamin, mineral, dan serat.'
        WHEN 'melon' THEN 'Sumber vitamin, mineral, dan serat.'
        WHEN 'semangka' THEN 'Sumber vitamin, mineral, dan membantu memenuhi kebutuhan cairan.'
        WHEN 'pisang' THEN 'Sumber karbohidrat, kalium, dan serat.'
        WHEN 'kelengkeng' THEN 'Sumber vitamin, mineral, dan serat.'
        WHEN 'anggur' THEN 'Sumber vitamin, mineral, dan antioksidan.'
        WHEN 'jeruk' THEN 'Sumber vitamin C, vitamin, dan serat.'

        WHEN 'tomat' THEN 'Sumber vitamin, mineral, dan antioksidan.'
        WHEN 'kol' THEN 'Sumber vitamin, mineral, dan serat.'
        WHEN 'sawi' THEN 'Sumber vitamin, mineral, dan serat.'
        WHEN 'timun' THEN 'Sumber vitamin, mineral, serat, dan air.'
        WHEN 'selada' THEN 'Sumber vitamin, mineral, dan serat.'
        WHEN 'wortel' THEN 'Sumber vitamin A, mineral, dan serat.'

        ELSE 'Kelompok pangan belum diklasifikasikan.'

    END;