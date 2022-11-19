SELECT 
		mahasiswa.id,
		mahasiswa.nama_mahasiswa,
		mahasiswa.nim_mahasiswa,
		mata_kuliah.nama_matkul
FROM
		mahasiswa
		INNER JOIN
		mata_kuliah
WHERE
		mahasiswa.rel_to_matkul = mata_kuliah.id