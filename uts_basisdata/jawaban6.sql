SELECT
		dosen.id,
		dosen.nama_dosen,
		dosen.kode_dosen,
		mahasiswa.nama_mahasiswa,
		mahasiswa.nim_mahasiswa,
		mata_kuliah.nama_matkul
FROM
		dosen
INNER JOIN
		mahasiswa, mata_kuliah
WHERE
		dosen.rel_to_mhs = mahasiswa.id AND dosen.rel_to_matkul = mata_kuliah.id