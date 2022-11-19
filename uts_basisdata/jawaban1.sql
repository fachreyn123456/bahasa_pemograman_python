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