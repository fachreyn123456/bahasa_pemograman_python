-- JAWABAN 1 --

CREATE TABLE mahasiswa(
		id INT AUTO_INCREMENT,
		nama_mahassiswa VARCHAR (255),
		nim_mahasiswa VARCHAR (255),
		rel_to_matkul INT,
		rel_to_dosen INT,
		PRIMARY KEY (id)
);

CREATE TABLE dosen(
		id INT AUTO_INCREMENT,
		nama_dosen VARCHAR (255),
		kode_dosen VARCHAR (255),
		rel_to_matkul INT,
		rel_to_mhs INT,
		PRIMARY KEY (id)
);

CREATE TABLE mata_kuliah(
		id INT AUTO_INCREMENT,
		nama_matkul VARCHAR (255),
		rel_to_dosen INT,
		rel_to_mhs INT,
		PRIMARY KEY (id)
);

-- JAWABAN 2 --
INSERT INTO mahasiswa (nama_mahasiswa, nim_mahasiswa) VALUES ('Rein', '20210801258'),('Rere', '20210801250');

INSERT INTO dosen (nama_dosen, kode_dosen) VALUES ('Hanan', '091'),('Rania','231');

INSERT INTO mata_kuliah (nama_matkul) VALUES ('basis data'),('bpo');

-- JAWABAN 3 --
SELECT * FROM mahasiswa

SELECT * FROM dosen

SELECT * FROM mata_kuliah

-- JAWABAN 4 --
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
		
-- JAWABAN 5 --
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
		
-- JAWABAN 6 --
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
		