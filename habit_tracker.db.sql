--
-- ���� ������������ � ������� SQLiteStudio v3.4.4 � �� ��� 19 13:00:52 2024
--
-- �������������� ��������� ������: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- �������: habit_progress
CREATE TABLE IF NOT EXISTS habit_progress (id INTEGER PRIMARY KEY AUTOINCREMENT, habit_id INTEGER, progress_date DATE, FOREIGN KEY (habit_id) REFERENCES habits (id));
INSERT INTO habit_progress (id, habit_id, progress_date) VALUES (1, 5, '2024-04-19');
INSERT INTO habit_progress (id, habit_id, progress_date) VALUES (2, 2, '2024-04-19');
INSERT INTO habit_progress (id, habit_id, progress_date) VALUES (3, 7, '2024-04-19');

-- �������: habits
CREATE TABLE IF NOT EXISTS habits (id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT, user_id INTEGER, habit_name TEXT, habit_description TEXT, habit_goal TEXT, habit_frequency TEXT, FOREIGN KEY (user_id) REFERENCES users (id));
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (1, 1, '���������� ����������', '��� ����� ���� ������, ���, ���� ��� ����� ������ ��� ������.', '������������� ���������� ����������, ����� �������� ��������, ���������� � ����� ������������.', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (2, 2, '���������� ��������', '��������� ���������� ������, ������� �����, �������� ����� ��� ���������� ����� ������', '��� ����������� ��� ���� � �������� ���������� ��������� ��������.', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (3, 3, '��������� ��� ����� �� �����������', '�������� ����� ������, ��������� ��� ������ �����������', '��������� ������ � �������� ���������� ��������', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (4, 1, '����������� ���', '���������� ����� 7-8 ����� ������ �����', '������������ ���������� �� ���� ����������,�������������� � ����� ��������', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (5, 1, '�������� �������', '��������������� ����������������� �������, ����������� ������, �����, ����� � ��������. ��������� ���������� � ��������', '�������� ��������,���������� � ����� ������������', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (7, 3, '���������� ��������', '��������� ���������� ������, ������� �����, �������� ����� ��� ���������� ����� ������', '��� ����������� ��� ���� � �������� ���������� ��������� ��������.', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (8, NULL, ' ������������� ??', '�������� ������� �������� ��� ������.', '��������� �������� � �������� �����', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (9, NULL, ' ��������������� ��������� ??', '������������� ��������� ��� ���������������� �������.', '����������� ����������� ������', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (10, NULL, ' ������������ ���������� ??', '����� ���������������� ����� � ����������.', '����������� ������������ ����������', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (11, NULL, ' ���������� ������� ??', '������������� ��� ��� ������������� ������.', '������������ ��������� ������� �������', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (12, NULL, ' ������������� ����� ����� ???', '��������� �� ������� � �����������.', '���������� ���������� ����������', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (13, NULL, ' ���������� ������������� �������� ��������� ??', '���� �� ������� � ����������� ���.', '����������� �������, ������������ ����� �������', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (14, NULL, ' �������������� ?', '���� �� ���������� � ��� "�����".', '��������� ������������������ � �������������', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (15, NULL, ' ���������� ��� ??', '��������� ��������� ������ �� ���.', '����������� ������������ � ������������� ���', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (16, NULL, ' ���������� ����������� ������� ?', '������ ������ �� ������������ �������.', '����������� ����������� �������', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (17, NULL, ' ����������� ��������� ??', '������������� �������� ��� ������.', '���������� �������� � ����������', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (18, NULL, ' ���������� ����������� � ���� � ������ ??', '���������� ���������� � ��������� � ����������.', '�������� � ������������� ��������� � ����', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (19, NULL, ' ������������� ������ ������� ??', '���� �� ������ � ���� � ������ �� �������.', '��������� �������� � ������������', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (20, NULL, ' ����� ??', '������������� ��� ��� ��������� ���������.', '���������� ������������� ���������', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (21, NULL, ' ���������� ������������ ������ ??', '������ ������������ ������������ �� �������.', '����������� ����������� ������', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (22, NULL, ' ��������� ��������� ������ ��� ������ ??', '����� ��������� � �������� ���� ��������.', '���������� � ���������� � ���������', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (23, NULL, ' �������� ??', '����� ������� �� �������� � ��� ������.', '������������ ���������� ������', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (24, NULL, ' ���������� ������� ������� �������� ??', '�������� ����������� ���� �� �������.', '������ � �������� ���� � ���', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (25, NULL, ' ������������� ������� �� ��������� ??', '����� �������� ���� ������ ��� �������.', '���� �� ����� � ����� ���������', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (26, NULL, ' ������������� ??', '���������� � ������ � ������ ��������.', '�������� ����������� � ���������� ��������', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (27, NULL, ' ����������� �� ������ ������ ??', '����� �� ����������� ����������.', '�������� ����������� ����������', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (28, NULL, ' ���������� ����������� �� �������� � ������ ??', '������������� ����� ��� ��������������� �����.', '���������� ���������� ����������', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (29, NULL, '���������� ������������������� ����� ����������� ??', '����� ������� � ���� ��������� �������.', '����������� ������� ����� �������', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (31, NULL, ' ���������� ������ ��� ��������������� ???', '����� �������������� � ������������ �����.', '���������� ��������� � �������������', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (32, NULL, '��������� �������������', '����� �� ���������� � ������������ �������������.', '�������� ��������������� �� ���� ��������', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (33, NULL, ' ���������� ������������ ���� ??', '������������� ���� ��� ������� ���������� ������.', '����������� ����������� ����', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (34, NULL, '������������� ������� � ����������� ��������� ??', '����� �������� ���� ����������.', '��������� �� ������� � ���������', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (35, NULL, '���������� � �������� � ��������� ������', '����� �������������� � ����� ���������.', '��������� �������� � ��������� � ����������', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (36, NULL, '������������� ���������� ���� � ������', '����� �� �������������� � ���������.', '�������� � ���������� ���������� ����', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (37, NULL, '��������������� ��������� ������������', '����� ���������� � ���� ������.', '������ ����� � �������������� �����������', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (38, NULL, '���������� ���������� ���������� ????>?', '�������� �������� ��� �������� � �������.', '��������� ���������� ����� � ������ ������������.', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (39, NULL, '�������� ������� ??', '�������, ������� ������������ ���������� � ����������.', '����������� ��������� ������ ����� � ������������ ����.', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (40, NULL, '����������� ��� ??', '����������� ����� ��� �������������� ���������.', '����������� �������� ������������������� � ����������� ���������.', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (41, NULL, '����� ������������ ���������� ���� ??', '������������ ������������ ������ ���� ��� ����������.', '����������� ��������� ������ ������� � ���������������� ���������.', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (42, NULL, '������ ���� ??', '���������������� �������� � ����� �� ��������������', '�������� ������������, ����������� � ����������� �������.', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (43, NULL, '��������� ��� ���� ??', '�������� ������������� � ������ �������.', '��������� ������������ �������� � ������ ����������.', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (44, NULL, '������������ ������ ������� ??', '����������� ������������� ������� ��� ���������� �����.', '��������� ������������������ � ����������� ������������ �����.', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (45, NULL, '������ �� ������ ������� ??', '���������� ���������� � ��������� ����������.', '��������� �������� � ����������, �������� �������.', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (46, NULL, '������ �������� "���" ??', '������ ���������� �� �������� ������������ � �������.', '������������ ������, ���������� ������� � ��������.', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (47, NULL, '���������� ����������� ������� ??', '����������� �������� � ������������� ��������� �������.', '������������ ����������� � ������ ��������� ��������������� �������.', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (50, NULL, '���������� ������� � ������� ??', '�������� ���������� � ������ ���������� � ����.', '��������� ����������� � ���������������� ������������.', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (51, NULL, '��������� ����������� �������� ??', '��������� ������������ ����������� �������� ��� ������������.', '����������� ��������� ������ ����� � ���������� ���������.', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (52, NULL, '���������� ����������� ���������� ??', '��������������� �������� � ��������� ����������.', '��������� �������������� ��������� � ��������� � �����������.', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (53, NULL, '������� � ������������ �������� ??', '������ � ��������� ������, �������� ����������� �������.', '�������������� �� �������������� � ���������� ������ � �����������.', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (54, NULL, '�������� ������������� ??', '���������� ��������� ������������� � ���������������.', '��������� ������ ������� � ��������� ������������ ���������.', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (55, NULL, '����� �� ������� ??', '����������� ����������� �������� �������.', '��������� �������� � �������� ����� �������� ��������� �����������.', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (56, NULL, '���������� ������� ???', '������������ ���������� �������� ��� ���������� �������.', '��������� ������������� ����������� ������� � �������� ������ �������', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (57, NULL, '�������� ����� ������� ??', '���������� ���������� ���� ������ �������� � ��������.', '�������� ��������, ���������� ��������� � ��������� ����������.', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (58, NULL, '����������� ���������� ������ ??', '������� � ������������ ����� � ����������� ���������', '��������� ������������� ��������� � �������� ��������������.', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (59, NULL, '������ � ����� ����������� �������� ??', '������������ ���� �� ����������� ���������� � ��������.', '���������� ��������������� ��������� � ���������� ��������.', '���������');
INSERT INTO habits (id, user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (60, NULL, '���������� ���������� ����� ??', '���������� ���������� � ��������������������� � �����.', '����������� ��������� � �������� �������������� � �����.', '���������');

-- �������: users
CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL);
INSERT INTO users (id, username) VALUES (1, '����');
INSERT INTO users (id, username) VALUES (2, '������');
INSERT INTO users (id, username) VALUES (3, '�����');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
