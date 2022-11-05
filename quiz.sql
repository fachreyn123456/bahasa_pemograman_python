CREATE TABLE mahasiswa(
	id INT AUTO_INCREMENT,
	nama_mahasiswa VARCHAR (255),
	rel_to_fak INT,
	rel_to_akre INT,
	rel_to_dos INT,
	PRIMARY KEY (id)
);

CREATE TABLE dosen(
	id INT AUTO_INCREMENT,
	nama_dosen VARCHAR (255),
	rel_to_mhs INT,
	rel_to_fak INT,
	rel_to_akre INT,
	PRIMARY KEY (id)
);

CREATE TABLE fakultas(
	id INT AUTO_INCREMENT,
	nama_fakultas VARCHAR (255),
	rel_to_mhs INT,
	rel_to_dosen INT,
	rel_to_akreditasi INT,
	PRIMARY KEY (id)
);

CREATE TABLE akreditasi(
	id INT AUTO_INCREMENT,
	nama_akreditasi VARCHAR (255),
	rel_to_fakultas INT,
	PRIMARY KEY (id)
);

CREATE TABLE matakuliah(
	id INT AUTO_INCREMENT,
	nama_matakuliah VARCHAR (255),
	rel_to_mahasiswa INT,
	rel_to_fakultas INT,
	rel_to_dosen INT,
	PRIMARY KEY (id)
);


INSERT INTO mahasiswa (nama_mahasiswa, nim_mahasiswa, jenis_kelamin) VALUES ('pradipta', 2021, 'laki-laki'),('riska', 2022, 'perempuan'),('lintang', 2023, 'laki-laki'),('luna', 2024, 'perempuan');

INSERT INTO dosen (kd_dosen, nama_dosen) VALUES ( 123, 'andre'),(234, 'ista'),(567, 'lisna');

INSERT INTO matakuliah (nama) VALUES ('basis data'),('bahasa pemograman'),('rpl');

INSERT INTO akreditasi (akreditasi) VALUES ('A'),('B');

INSERT INTO fakultas (nama_fakultas, kd_fakultas) VALUES ('Teknik Informatika', 'cr101'),('Sistem Operasi', 'kj202');


-- JAWABAN 1--
SELECT * FROM mahasiswa

SELECT * FROM dosen

SELECT * FROM matakuliah

SELECT * FROM fakultas

SELECT * FROM akreditasi

-- JAWABAN 2 --
SELECT
	mahasiswa.id,
	mahasiswa.nama_mahasiswa,
	mahasiswa.nim_mahasiswa,
	mahasiswa.jenis_kelamin,
	fakultas.nama_fakultas,
	fakultas.kd_fakultas
FROM
	mahasiswa
	INNER JOIN
	fakultas
WHERE
	mahasiswa.rel_to_fak = fakultas.id

-- JAWABAN 3 --
SELECT
	mahasiswa.id,
	mahasiswa.nama_mahasiswa,
	mahasiswa.nim_mahasiswa,
	mahasiswa.jenis_kelamin,
	fakultas.nama_fakultas,
	fakultas.kd_fakultas,
	akreditasi.akreditasi
FROM
	mahasiswa
INNER JOIN
	fakultas, akreditasi
WHERE
	mahasiswa.rel_to_fak = fakultas.id AND mahasiswa.rel_to_akre = akreditasi.id

-- JAWABAN 4 --
SELECT
	dosen.id,
	dosen.nama_dosen,
	dosen.kd_dosen,
	mahasiswa.id,
	mahasiswa.nama_mahasiswa,
	mahasiswa.nim_mahasiswa,
	mahasiswa.jenis_kelamin
FROM
	dosen
INNER JOIN
	mahasiswa
WHERE
	dosen.rel_to_mhs = dosen.id

-- JAWABAN 5 --
SELECT
	dosen.id,
	dosen.nama_dosen,
	dosen.kd_dosen,
	fakultas.nama_fakultas,
	fakultas.kd_fakultas,
	akreditasi.akreditasi
FROM
	dosen
INNER JOIN
	fakultas, akreditasi
WHERE
	dosen.rel_to_fak = fakultas.id AND dosen.rel_to_akre = akreditasi.id

	
	
	

	
	