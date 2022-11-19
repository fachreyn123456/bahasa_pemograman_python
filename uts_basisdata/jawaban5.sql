SELECT
		dosen.id,
		dosen.nama_dosen,
		dosen.kode_dosen,
		mata_kuliah.nama_matkul
FROM
		dosen
		INNER JOIN
		mata_kuliah
WHERE
		dosen.rel_to_matkul = mata_kuliah.id