-- Prazos das Entregas --
INSERT INTO version (version_name, direct_input, extension, date_from, date_to) VALUES("v0.1", 1, ".txt", "2022-08-15 15:45:00", "2022-08-22 13:30:00");
INSERT INTO version (version_name, direct_input, extension, date_from, date_to) VALUES("v1.0", 1, ".txt", "2022-08-22 15:45:00", "2022-08-29 13:30:00");
INSERT INTO version (version_name, direct_input, extension, date_from, date_to) VALUES("v1.1", 1, ".txt", "2022-08-29 15:45:00", "2022-09-05 13:30:00");
INSERT INTO version (version_name, direct_input, extension, date_from, date_to) VALUES("v1.2", 1, ".txt", "2022-09-05 15:45:00", "2022-09-12 13:30:00");
INSERT INTO version (version_name, direct_input, extension, date_from, date_to) VALUES("v2.0", 0, ".c", "2022-09-12 15:45:00", "2022-09-19 13:30:00");
INSERT INTO version (version_name, direct_input, extension, date_from, date_to) VALUES("v2.1", 0, ".c", "2022-09-19 15:45:00", "2022-09-26 13:30:00");
INSERT INTO version (version_name, direct_input, extension, date_from, date_to) VALUES("v2.2", 0, ".c", "2022-10-10 15:45:00", "2022-10-24 13:30:00");
INSERT INTO version (version_name, direct_input, extension, date_from, date_to) VALUES("v2.3", 0, ".c", "2022-10-24 15:45:00", "2022-11-07 13:30:00");
INSERT INTO version (version_name, direct_input, extension, date_from, date_to) VALUES("v3.0", 0, ".c", "2022-11-07 15:45:00", "2022-11-16 13:30:00");
INSERT INTO version (version_name, direct_input, extension, date_from, date_to) VALUES("v2.4", 0, ".c", "2022-11-16 15:45:00", "2022-11-30 13:30:00");

-- Usuarios --
INSERT INTO users (git_username, name, surname) VALUES("macielcalebe", "Maciel", "Calebe Vidal");
INSERT INTO users (git_username, name, surname) VALUES("FelippeTeracini", "Felippe", "Teracini");

-- Repos --
INSERT INTO repository (git_username, repository_name, language, compiled, program_call) VALUES("FelippeTeracini", "WebhookTest3", "python", 0, "python3 main.py");

INSERT INTO repository (git_username, repository_name, language, compiled, program_call) VALUES("macielcalebe", "comp1", "python", 0, "python3 main.py");
INSERT INTO repository (git_username, repository_name, language, compiled, program_call) VALUES("macielcalebe", "comp2", "python", 0, "python3 main.py");

-- Alunos Exemplo:
INSERT INTO users (git_username, name, surname) VALUES("Pellizzon", "MATHEUS", "PELLIZZON");
INSERT INTO users (git_username, name, surname) VALUES("gabrielztk", "GABRIEL", "ZANETTI TRAUMULLER KAWALL");
INSERT INTO users (git_username, name, surname) VALUES("manucastilla", "MANUELA", "CASTILLA RUSSO CORREA");
INSERT INTO users (git_username, name, surname) VALUES("gicabral", "GIOVANNA", "SARDELLA CABRAL");

INSERT INTO repository (git_username, repository_name, language, compiled, program_call) VALUES("manucastilla", "roteiros_logicaComputacao", "python", 0, "python3 main.py");
INSERT INTO repository (git_username, repository_name, language, compiled, program_call) VALUES("Pellizzon", "LogicaDaComputacao", "python", 0, "python3 main.py");
INSERT INTO repository (git_username, repository_name, language, compiled, program_call) VALUES("gicabral", "Logica-Computacao", "python", 0, "python3 main.py");
INSERT INTO repository (git_username, repository_name, language, compiled, program_call) VALUES("gabrielztk", "LogiComp2021.1-Compilador", "python", 0, "python3 main.py");


