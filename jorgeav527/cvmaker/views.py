from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

from weasyprint import HTML

# from weasyprint.fonts import FontConfiguration

NAME = "jorge ramiro alarcón vargas"
SELF_THOUGHT = "full stack developer"
BOOTCAMP = "data scientist"
PHONE = +51973635864
GITHUB = "jorgeav527"
LINKEDIN = "jorgeav527"
GMAIL = "jorgeav527@gmail.com"
UNIVERSITY = "Universidad Católica de Santa María"
CIP = 257513
UNI_START = 2008
UNI_END = 2014
UNI_LOCATION = "Arequipa - Perú"


def english_pdf_view(request):
    EXPERIENCE = "work experience"
    PROFF = "civil engineer"
    EDUCATION = "education"
    LANGUAGE = "languages"
    SKILL = "skill & tools"
    FEATURED = "Featured"
    VOLUNTER = "Volunteering"
    ABOUT = "about me"
    PROJECT = "projects"
    ABOUT_DESCRIPTION = [
        "I'm a Civil Engineer with a focus on Data Science and solid foundations in Web Development, a C1 advanced level of English, and international experience in Brazil.",
        "Since 2018, I've been gradually immersing myself in the world of technology. I worked as a freelancer using programming languages, databases, and web development environments to automate processes in the field of civil engineering.",
        "Actually, I extract, analyze, and model data using Data Science and Machine Learning principles. I build viable and scalable data flow architectures with Airflow. I orchestrate various cloud services on the Linode platform and generate insights using data visualization tools such as PowerBI or Streamlit.",
    ]
    VOL_ORGANIZATION = "AIESEC en Colombia"
    VOL_DESCRIPTION = "9000xBogota is an AIESEC initiative that demonstrates to the citizens of Bogotá that young people of various nationalities can feel empathy and respect for the city that becomes their temporary home, while also raising social awareness and providing information about the importance of global warming."
    VOL_NAME = "Universidad de los Andes, Colombia: 7000xBogotá"
    VOL_START = "Dec 2010"
    VOL_END = "Mar 2011"
    VOL_LOCATION = "Bogota Colombia"
    LANG_DICT = {
        "english": "Professional working proficiency",
        "portugues": "Full professional proficiency",
        "spanish": "Native or bilingual proficiency",
    }
    FEATURED_DICT = {
        "II INTERNATIONAL CONGRESS OF CIVIL ENGINEERING II CIDEIC UCSM 2021": {
            "title": 'SPEAKER "Web Development for Civil Engineer"',
            "location": "Arequipa, Arequipa, Perú",
            "start": "Nov 2021",
            "end": "Nov 2021",
            "responsibilities": [
                'On November 15-19, 2021, the Private Catholic University of Santa María from Arequipa, Peru, hosted the "II INTERNATIONAL CONGRESS OF CIVIL ENGINEERING STUDENTS".',
                "Topics: operating systems, introduction to the Command-line interface (CLI), basic concepts of the IOT, characteristics of the Front-End and Back-End, introduction to SQL databases, demonstration of the development and deployment of a project, final but not least a live demonstration of the most popular CVS tool (Git & GitHub).",
            ],
        }
    }
    PROJECT_DICT = {
        "Machine Learning Specialization": {
            "title": "Datathon - Applying ML Modeling",
            "link": "https://github.com/jorgeav527/Datathon.git",
            "start": "Sep 2022",
            "end": "Present",
            "techstack": [
                "Jupyter (Numpy & Pandas & Scikit-Learn & Plotly).",
            ],
        },
        "Final project for Henry's Data Science Bootcamp": {
            "title": "Life Expectancy - ETL & EDA & ML",
            "link": "https://github.com/jorgeav527/life-expectancy.git",
            "start": "Sep 2022",
            "end": "Oct 2022",
            "techstack": [
                "OS Linux, Git & GitHub & Git LFS, Jupyter (Numpy & Pandas & Scikit-Learn, Matplotlib), Heroku, MongoDB, ElephantSQL, FastAPI, Streamlit, Apache Airflow, Docker, Linode (EC2 & RDS & S3)."
            ],
        },
        "RPG Labs - Grupo RPG SAC": {
            "title": "Web Application for Testing Services at a Civil Engineering Soils Laboratory",
            "link": "https://github.com/jorgeav527/rpg_labs_repo.git",
            "start": "Dec 2021",
            "end": "Mar 2022",
            "techstack": [
                "OS Linux, Git & GitHub (GitHub Flow), HTML, CSS-BootstrapMade, Django, HTMX, Nginx, Bash, Docker, Html2pdf, PostgreSQL, AWS (EC2 & RDS & S3)."
            ],
        },
        "EPIC Labs - Professional Thesis Degree": {
            "title": "Thesis: Civil Engineering Laboratory Automation and Systematization",
            "location": "Arequipa, Arequipa, Perú",
            "link": "https://github.com/jorgeav527/epiclabs.git",
            "start": "Dec 2019",
            "end": "Dec 2020",
            "techstack": [
                "OS Linux, Git & GitHub, HTML, CSS-Bootstrap, Django, Matplotlib & Bokeh, WeasyPrint, SQLite, PythonAnywhere."
            ],
        },
    }
    EXP_DICT = {
        "Grupo RPG SAC": {
            "title": 'Civil Engineer "Soils Laboratory IT Automation"',
            "location": "Tiabaya, Arequipa, Perú",
            "type": "Freelance",
            "start": "Dec 2021",
            "end": "Mar 2022",
            "responsibilities": [
                'The web application in the FIRST MODULE "QUOTES" has the ability to register customers and generate quotes for the required tests. Create a service order and a settlement sheet for the tests that were performed.',
                "I had planned and performed the analysis of information, designed, developed, and deployed a web application tool that meets the requirements and needs of the laboratory.",
                "I had built a Docker virtual space that was mounted on an EC2 instance running on AWS servers, using RDS for relational database backup and restore, and S3 bucket store for images and PDF reports.",
            ],
        },
        "Municipalidad Distrital de Majes": {
            "title": "Civil Engineer",
            "location": "Majes, Arequipa, Perú",
            "type": "Full-time",
            "start": "May 2021",
            "end": "Nov 2021",
            "responsibilities": [
                "Assistance in the reporting and review of technical-financial liquidations of public investment projects, identification and registration of Public Investments (IOARR), in accordance with the Payment Services Directive of the State Contracting Law.",
                "Review and report on the additional, deductive, and investment extensions of public projects.",
                "Monthly review of waste generated in public projects and appropriate waste recovery.",
                "Monitoring and updating the management and schedule of various public projects via online web platforms (Form 12B).",
            ],
        },
        "Juares Arquitectos & Ingenieros SAC": {
            "title": "Civil Engineer",
            "location": "Arequipa, Arequipa, Perú",
            "type": "Freelance",
            "start": "Nov 2018",
            "end": "Nov 2019",
            "responsibilities": [
                "Professional support on technical and structural details of buildings and retaining walls.",
                "Daily, weekly, and monthly detailed efficient control of the schedule work through the MS Project tool.",
                "Reporting monthly work valuations, presented in Excel.",
            ],
        },
        "FourC Bilingual Academy": {
            "title": "Engineer Building Maintenance",
            "location": "Bauru, São Paulo, Brazil",
            "type": "Internship",
            "start": "Jun 2016",
            "end": "Dec 2017",
            "responsibilities": [
                "Professional support in solving construction defects with forecasts and multiple solutions.",
                "Detailed and efficient control of the maintenance team's daily, weekly, and monthly task schedule with MS Project.",
                "I reduced drinking water consumption by 30% and monthly electricity consumption by 11% by using pre-existing data.",
            ],
        },
    }
    SKILL_DICT = {
        "data science": [
            "JupyterLab",
            "Numpy",
            "Pandas",
            "Scikit-Learn",
            "PyTorch",
            "Mongo",
            "Cassandra",
            "neo4j",
            "Apache Hadoop",
            "Apache Spark",
            "Apache Airflow",
            "Databricks",
            "Docker",
            "Streamlit",
            "PowerBI",
        ],
        "Full Stack Development": [
            "OS Linux",
            "Bash",
            "Vuejs",
            "Node",
            "Django",
            "Flask",
            "HTMX",
            "FastAPIiii",
            "Git & GitHub",
            "Jupyter Notebook",
            "PostgreSQL & MySQL",
            "Docker",
            "AWS (EC2 & RDS & S3)",
            "Linode",
        ],
        "Civil Background": [
            "Excel",
            "MS-Project",
            "AutoCad",
            "Civil3D",
            "Revit",
            "ArcGis",
            "QGis",
            "SAP2000",
            "BIM",
        ],
    }

    context = {
        "name": NAME,
        "proff": PROFF,
        "self_thought": SELF_THOUGHT,
        "bootcamp": BOOTCAMP,
        "phone": PHONE,
        "github": GITHUB,
        "linkedin": LINKEDIN,
        "gmail": GMAIL,
        "experience": EXPERIENCE,
        "exp_dict": EXP_DICT,
        "education": EDUCATION,
        "university": UNIVERSITY,
        "cip": CIP,
        "uni_start": UNI_START,
        "uni_end": UNI_END,
        "uni_location": UNI_LOCATION,
        "lang_dict": LANG_DICT,
        "language": LANGUAGE,
        "skill": SKILL,
        "skill_dict": SKILL_DICT,
        "volunter": VOLUNTER,
        "vol_organization": VOL_ORGANIZATION,
        "vol_description": VOL_DESCRIPTION,
        "vol_name": VOL_NAME,
        "vol_start": VOL_START,
        "vol_end": VOL_END,
        "vol_location": VOL_LOCATION,
        "featured": FEATURED,
        "featured_dict": FEATURED_DICT,
        "about": ABOUT,
        "about_description": ABOUT_DESCRIPTION,
        "project": PROJECT,
        "project_dict": PROJECT_DICT,
    }
    html = render_to_string("cvmaker/first.html", context)

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "inline; report.pdf"

    # font_config = FontConfiguration()
    HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(response)

    return response


def spanish_pdf_view(request):
    EXPERIENCE = "experiencia"
    PROFF = "ingeniero civil"
    EDUCATION = "educación"
    LANGUAGE = "idiomas"
    SKILL = "competencias"
    FEATURED = "destacado"
    VOLUNTER = "voluntariado"
    ABOUT = "acerca de"
    PROJECT = "proyectos"
    ABOUT_DESCRIPTION = [
        "Ingeniero Civil con foco en Ciencia de Datos y profundo conocimiento en Desarrollo Web, con un nivel de inglés C1 Avanzado y con experiencia internacional en Brasil.",
        "Desde 2018 me introduje gradualmente en el mundo de la tecnología, trabajé como freelance usando lenguajes de programación, bases de datos y entornos virtuales para automatizar procesos en el campo de la ingeniería civil.",
        "Actualmente, extraigo, analizo y modelo información usando los principios del Data Science y Machine Learning. Diseño arquitecturas viables y escalables para el flujo de los datos con Airflow. Orquesto diferentes servicios en la nube y genero información valiosa a través de herramientas de visualización como PowerBI o Streamlit.",
    ]
    VOL_ORGANIZATION = "AIESEC en Colombia"
    VOL_DESCRIPTION = "9000xBogota una iniciativa de AIESEC para mostrar a los ciudadanos de Bogotá, que jóvenes de diferentes nacionalidades pueden sentir empatía y respeto por la ciudad que brevemente los acoge, ofreciendo conciencia social e información de la importancia del calentamiento global."
    VOL_NAME = "Universidad de los Andes, Colombia: 7000xBogotá"
    VOL_START = "Dec 2010"
    VOL_END = "Mar 2011"
    VOL_LOCATION = "Bogota Colombia"
    LANG_DICT = {
        "Inglés": "Habilidad de trabajo profesional",
        "Protugués": "Competencia profesional completa",
        "Español": "Competencia bilingüe o nativa",
    }
    FEATURED_DICT = {
        "II CONCRESO INTERNACIONAL DE INGENIERIA CIVIL CIDEIC UCSM 2021": {
            "title": 'PONENTE "Desarrollo Web para Ingeniería Civil"',
            "location": "Arequipa, Arequipa, Perú",
            "start": "Nov 2021",
            "end": "Nov 2021",
            "responsibilities": [
                "Del 15 al 19 de noviembre del 2021, la Universidad Católica de Santa María de Arequipa, Perú, fue sede del “II CONGRESO INTERNACIONAL DE ESTUDIANTES DE INGENIERÍA CIVIL”.",
                "Temas: sistemas operativos, introducción a la interfaz de línea de comando (CLI), conceptos básicos del IOT, características del Front-End y Back-End, introducción a bases de datos SQL, demostración del desarrollo y despliegue de un proyecto, y por último una demostración en vivo de la herramienta Git y GitHub.",
            ],
        }
    }
    PROJECT_DICT = {
        "Especialización en Machine Learning": {
            "title": "Datathon - Aplicación de modelos en ML",
            "link": "https://github.com/jorgeav527/Datathon.git",
            "start": "Sep 2022",
            "end": "Present",
            "techstack": [
                "Jupyter (Numpy & Pandas & Scikit-Learn & Plotly).",
            ],
        },
        "Proyecto Final - Bootcamp de Henry en Data Science": {
            "title": "Esperanza de Vida - ETL & EDA & ML",
            "link": "https://github.com/jorgeav527/life-expectancy.git",
            "start": "Sep 2022",
            "end": "Oct 2022",
            "techstack": [
                "OS Linux, Git & GitHub & Git LFS, Jupyter (Numpy & Pandas & Scikit-Learn, Matplotlib), Heroku, MongoDB, ElephantSQL, FastAPI, Streamlit, Apache Airflow, Docker, Linode (EC2 & RDS & S3)."
            ],
        },
        "RPG Labs - Grupo RPG SAC": {
            "title": "Aplicación Web para Servicios de Ensayos en los Laboratorios de Suelos de Ingeniería Civil",
            "link": "https://github.com/jorgeav527/rpg_labs_repo.git",
            "start": "Dec 2021",
            "end": "Mar 2022",
            "techstack": [
                "OS Linux, Git & GitHub (GitHub Flow), HTML, CSS-BootstrapMade, Django, HTMX, Nginx, Bash, Docker, Html2pdf, PostgreSQL, AWS (EC2 & RDS & S3)."
            ],
        },
        "EPIC Labs - Tesis de Grado Profesional": {
            "title": "Automatización y Sistematización de los Laboratorios de Ingeniería Civil",
            "location": "Arequipa, Arequipa, Perú",
            "link": "https://github.com/jorgeav527/epiclabs.git",
            "start": "Dec 2019",
            "end": "Dec 2020",
            "techstack": [
                "OS Linux, Git & GitHub, HTML, CSS-Bootstrap, Django, Matplotlib & Bokeh, WeasyPrint, SQLite, PythonAnywhere."
            ],
        },
    }
    EXP_DICT = {
        "Grupo RPG SAC": {
            "title": 'Ingeniero Civil "Automatización de procesos en el Laboratorio de Suelos"',
            "location": "Tiabaya, Arequipa, Perú",
            "type": "Freelance",
            "start": "Dec 2021",
            "end": "Mar 2022",
            "responsibilities": [
                'En el PRIMER MÓDULO "COTIZACIONES" la aplicación tiene la capacidad de registrar a los clientes y realizar cotizaciones de los ensayos requeridos para luego generar una orden de servicio y una hoja de liquidación de los ensayos ejecutados.',
                "Análisis de información, diseño, desarrollo y despliegue de una herramienta web que se ajuste a los requerimientos del laboratorio.",
                "Creación de un espacio virtual con Docker, montado en una instancia EC2 en los servidores de AWS, RDS para la base de datos relacional Backup & Restore y S3 para las imágenes y reportes en PDF.",
            ],
        },
        "Municipalidad Distrital de Majes": {
            "title": "Ingeniero Civil",
            "location": "Majes, Arequipa, Perú",
            "type": "Jornada Completa",
            "start": "May 2021",
            "end": "Nov 2021",
            "responsibilities": [
                "Asistencia en la elaboración y revisión de liquidaciones técnico financiera de proyectos de inversión pública e IOARR, Conforme a la directiva de Liquidación de la Ley de Contrataciones del Estado.",
                "Tramite de las modificaciones en ejecución de obra Formato 8A de adicionales, deductivos y ampliaciones de plazo de las Inversiones de la Municipalidad.",
                "Revisión de las valorizaciones mensuales de obras.",
                "Seguimiento y actualización de las obras en las plataformas del Invierte.pe Formato 12B.",
            ],
        },
        "Juares Arquitectos & Ingenieros SAC": {
            "title": "Ingeniero Civil",
            "location": "Arequipa, Arequipa, Perú",
            "type": "Freelance",
            "start": "Nov 2018",
            "end": "Nov 2019",
            "responsibilities": [
                "Soporte profesional en el área técnica estructural en edificaciones y muros de contención.",
                "Control detallado y eficiente de las tareas diarias, semanales y mensuales de obra a través de la herramienta MS Project.",
                "Elaboración de las valorizaciones mensuales de obra, automatizado en Excel.",
            ],
        },
        "FourC Bilingual Academy": {
            "title": "Ingeniero de Mantenimiento de Estructura",
            "location": "Bauru, São Paulo, Brazil",
            "type": "Internship",
            "start": "Jun 2016",
            "end": "Dec 2017",
            "responsibilities": [
                "Soporte profesional para la solución de vicios estructurales con pronósticos y soluciones múltiples.",
                "Control detallado y eﬁciente de las tareas diarias, semanales y mensuales del personal de mantenimiento, a través de la herramienta MS Project.",
                "Reducí en 30% el consumo de agua potable y en 11% el consumo de energía eléctrica mensual.",
            ],
        },
    }
    SKILL_DICT = {
        "data science": [
            "JupyterLab",
            "Numpy",
            "Pandas",
            "Scikit-Learn",
            "PyTorch",
            "Mongo",
            "Cassandra",
            "neo4j",
            "Apache Hadoop",
            "Apache Spark",
            "Apache Airflow",
            "Databricks",
            "Docker",
            "Streamlit",
            "PowerBI",
        ],
        "Full Stack Development": [
            "OS Linux",
            "Bash",
            "Vuejs",
            "Node",
            "Django",
            "Flask",
            "HTMX",
            "FastAPIiii",
            "Git & GitHub",
            "Jupyter Notebook",
            "PostgreSQL & MySQL",
            "Docker",
            "AWS (EC2 & RDS & S3)",
            "Linode",
        ],
        "Ingeniería Civil": [
            "Excel",
            "MS-Project",
            "AutoCad",
            "Civil3D",
            "Revit",
            "ArcGis",
            "QGis",
            "SAP2000",
            "BIM",
        ],
    }

    context = {
        "name": NAME,
        "proff": PROFF,
        "self_thought": SELF_THOUGHT,
        "bootcamp": BOOTCAMP,
        "phone": PHONE,
        "github": GITHUB,
        "linkedin": LINKEDIN,
        "gmail": GMAIL,
        "experience": EXPERIENCE,
        "exp_dict": EXP_DICT,
        "education": EDUCATION,
        "university": UNIVERSITY,
        "cip": CIP,
        "uni_start": UNI_START,
        "uni_end": UNI_END,
        "uni_location": UNI_LOCATION,
        "lang_dict": LANG_DICT,
        "language": LANGUAGE,
        "skill": SKILL,
        "skill_dict": SKILL_DICT,
        "volunter": VOLUNTER,
        "vol_organization": VOL_ORGANIZATION,
        "vol_description": VOL_DESCRIPTION,
        "vol_name": VOL_NAME,
        "vol_start": VOL_START,
        "vol_end": VOL_END,
        "vol_location": VOL_LOCATION,
        "featured": FEATURED,
        "featured_dict": FEATURED_DICT,
        "about": ABOUT,
        "about_description": ABOUT_DESCRIPTION,
        "project": PROJECT,
        "project_dict": PROJECT_DICT,
    }
    html = render_to_string("cvmaker/first.html", context)

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "inline; report.pdf"

    # font_config = FontConfiguration()
    HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(response)

    return response


def portuguese_pdf_view(request):
    EXPERIENCE = "experiência"
    PROFF = "engenheiro civil"
    EDUCATION = "formação"
    LANGUAGE = "idiomas"
    SKILL = "competências"
    FEATURED = "em destaque"
    VOLUNTER = "voluntariado"
    ABOUT = "sobre"
    PROJECT = "projetos"
    ABOUT_DESCRIPTION = [
        "Engenheiro Civil com foco em ciências de dados e um vasto conhecimento em Desenvolvimento Web. Nível de inglês C1 Avançado e experiência internacional no Brasil.",
        "Desde 2018 me inserir gradualmente no mundo da tecnologia, trabalhei como freelance usando linguagens de programações, bases de dados e entornos virtuais para automatizar os processos no  campo da engenharia civil.",
        "Atualmente, extraio, analiso e modelo informações usando os princípios de Data Science e Machine Learning. Projeto arquiteturas viáveis e escaláveis para o fluxo dos dados, orquestro diferentes serviços em nuvem, gerando informações valiosas através de ferramentas de visualização como PowerBI ou Streamlit.",
    ]
    VOL_ORGANIZATION = "AIESEC en Colombia"
    VOL_DESCRIPTION = "9000xBogotá uma iniciativa da AIESEC para mostrar aos cidadãos de Bogotá, que jovens de diferentes nacionalidades podem sentir empatia e respeito pela cidade que brevemente os acolhe, oferecendo consciência sociais e informações sobre a importância da aquecimento global."
    VOL_NAME = "Universidad de los Andes, Colombia: 7000xBogotá"
    VOL_START = "Dec 2010"
    VOL_END = "Mar 2011"
    VOL_LOCATION = "Bogota Colombia"
    LANG_DICT = {
        "Inglês": "Habilidade de trabalho profissional",
        "Português": "Competência profissional completa",
        "Espanhol": "Proficiência bilíngue ou nativa",
    }
    FEATURED_DICT = {
        "II CONCRESO INTERNACIONAL DE INGENIERIA CIVIL CIDEIC UCSM 2021": {
            "title": 'PALESTRANTE "Desenvolvimento Web para Engenharia Civil"',
            "location": "Arequipa, Arequipa, Perú",
            "start": "Nov 2021",
            "end": "Nov 2021",
            "responsibilities": [
                'De 15 a 19 de novembro de 2021, a Universidade Católica de Santa María de Arequipa, Peru, sediou o "II CONGRESSO INTERNACIONAL DE ESTUDANTES DE ENGENHARIA CIVIL".',
                "Tópicos: sistemas operativos, introdução à interface de linha de comando (CLI), noções básicas de IOT, caracteristicas de front-end e back-end, introdução no bancos de dados SQL, demonstração de desenvolvimento e implantação de um projeto e por último, uma demonstração ao vivo da ferramenta Git e GitHub.",
            ],
        }
    }
    PROJECT_DICT = {
        "Especialização em Machine Learning": {
            "title": "Datathon - Aplicação de modelos em ML",
            "link": "https://github.com/jorgeav527/Datathon.git",
            "start": "Sep 2022",
            "end": "Present",
            "techstack": [
                "Jupyter (Numpy & Pandas & Scikit-Learn & Plotly).",
            ],
        },
        "Projeto Final - Bootcamp de Henry em Data Science": {
            "title": "Esperança na vida - ETL & EDA & ML",
            "link": "https://github.com/jorgeav527/life-expectancy.git",
            "start": "Sep 2022",
            "end": "Oct 2022",
            "techstack": [
                "OS Linux, Git & GitHub & Git LFS, Jupyter (Numpy & Pandas & Scikit-Learn, Matplotlib), Heroku, MongoDB, ElephantSQL, FastAPI, Streamlit, Apache Airflow, Docker, Linode (EC2 & RDS & S3)."
            ],
        },
        "RPG Labs - Grupo RPG SAC": {
            "title": "Aplicativo Web para Serviços de Teste nos Laboratórios de Solos da Engenharia Civil",
            "link": "https://github.com/jorgeav527/rpg_labs_repo.git",
            "start": "Dec 2021",
            "end": "Mar 2022",
            "techstack": [
                "OS Linux, Git & GitHub (GitHub Flow), HTML, CSS-BootstrapMade, Django, HTMX, Nginx, Bash, Docker, Html2pdf, PostgreSQL, AWS (EC2 & RDS & S3)."
            ],
        },
        "EPIC Labs - Tese de Formatura": {
            "title": "Automação e Sistematização dos Laboratórios da Engenharia Civil",
            "location": "Arequipa, Arequipa, Perú",
            "link": "https://github.com/jorgeav527/epiclabs.git",
            "start": "Dec 2019",
            "end": "Dec 2020",
            "techstack": [
                "OS Linux, Git & GitHub, HTML, CSS-Bootstrap, Django, Matplotlib & Bokeh, WeasyPrint, SQLite, PythonAnywhere."
            ],
        },
    }
    EXP_DICT = {
        "Grupo RPG SAC": {
            "title": 'Engenheiro Civil "Automação de processos no Laboratório de Solos"',
            "location": "Tiabaya, Arequipa, Perú",
            "type": "Freelance",
            "start": "Dec 2021",
            "end": "Mar 2022",
            "responsibilities": [
                'No primer MÓDULO "ORÇAMENTO" o aplicativo tem a capacidade de cadastrar clientes e fazer cotações para o testes necessários para então gerar uma ordem de serviço e uma folha de liquidação dos testes realizados.',
                "Análise de informações, desenho, desenvolvimento e implantação de uma ferramenta web que atende aos requisitos do laboratório.",
                "Criação de um espaço virtual com Docker, montado em instância EC2 em servidores AWS, RDS pelo banco de dados relacional Backup & Restore e S3 bucket pelas imagens e orcamentos em PDF.",
            ],
        },
        "Prefeitura Provincial de Majes": {
            "title": "Engenheiro Civil",
            "location": "Majes, Arequipa, Perú",
            "type": "Jornada Completa",
            "start": "May 2021",
            "end": "Nov 2021",
            "responsibilities": [
                "Assessoria na preparação e revisão de liquidações técnicas financeiras de projetos de investimento público e IOARR, de acordo com a diretiva de Liquidação da Lei de Aprovisionamento do Estado.",
                "Processamento de modificações na execução da obra Formato 8A de adicionais, dedutivos e prorrogativos de prazo dos Investimentos da Prefeitura.",
                "Revisão das avaliações mensais das obras.",
                "Acompanhamento e atualização das obras nas plataformas de Invierte.pe Formato 12B.",
            ],
        },
        "Juares Arquitectos & Ingenieros SAC": {
            "title": "Engenheiro Civil",
            "location": "Arequipa, Arequipa, Perú",
            "type": "Freelance",
            "start": "Nov 2018",
            "end": "Nov 2019",
            "responsibilities": [
                "Soporte profissional na área técnica estrutural em edifícios e muros de contenção.",
                "Controle detalhado e eficiente das tarefas diárias, semanais e mensais através da ferramenta MS Project.",
                "Elaboração de avaliações do trabalho mensais, automatizadas em Excel.",
            ],
        },
        "FourC Bilingual Academy": {
            "title": "Engenheiro de Manutenção de Estruturas",
            "location": "Bauru, São Paulo, Brazil",
            "type": "Estágio",
            "start": "Jun 2016",
            "end": "Dec 2017",
            "responsibilities": [
                "Suporte profissional para a solução de defeitos estruturais com opções em previsões e soluções.",
                "Controle detalhado e eficiente das tarefas diárias, semanais e mensais do pessoal de manutenção, através da ferramenta MS Project.",
                "Reduzi o consumo de água potável em 30% e o consumo mensal de eletricidade em 11%.",
            ],
        },
    }
    SKILL_DICT = {
        "data science": [
            "JupyterLab",
            "Numpy",
            "Pandas",
            "Scikit-Learn",
            "PyTorch",
            "Mongo",
            "Cassandra",
            "neo4j",
            "Apache Hadoop",
            "Apache Spark",
            "Apache Airflow",
            "Databricks",
            "Docker",
            "Streamlit",
            "PowerBI",
        ],
        "Full Stack Development": [
            "OS Linux",
            "Bash",
            "Vuejs",
            "Node",
            "Django",
            "Flask",
            "HTMX",
            "FastAPIiii",
            "Git & GitHub",
            "Jupyter Notebook",
            "PostgreSQL & MySQL",
            "Docker",
            "AWS (EC2 & RDS & S3)",
            "Linode",
        ],
        "Engenharia Civil": [
            "Excel",
            "MS-Project",
            "AutoCad",
            "Civil3D",
            "Revit",
            "ArcGis",
            "QGis",
            "SAP2000",
            "BIM",
        ],
    }

    context = {
        "name": NAME,
        "proff": PROFF,
        "self_thought": SELF_THOUGHT,
        "bootcamp": BOOTCAMP,
        "phone": PHONE,
        "github": GITHUB,
        "linkedin": LINKEDIN,
        "gmail": GMAIL,
        "experience": EXPERIENCE,
        "exp_dict": EXP_DICT,
        "education": EDUCATION,
        "university": UNIVERSITY,
        "cip": CIP,
        "uni_start": UNI_START,
        "uni_end": UNI_END,
        "uni_location": UNI_LOCATION,
        "lang_dict": LANG_DICT,
        "language": LANGUAGE,
        "skill": SKILL,
        "skill_dict": SKILL_DICT,
        "volunter": VOLUNTER,
        "vol_organization": VOL_ORGANIZATION,
        "vol_description": VOL_DESCRIPTION,
        "vol_name": VOL_NAME,
        "vol_start": VOL_START,
        "vol_end": VOL_END,
        "vol_location": VOL_LOCATION,
        "featured": FEATURED,
        "featured_dict": FEATURED_DICT,
        "about": ABOUT,
        "about_description": ABOUT_DESCRIPTION,
        "project": PROJECT,
        "project_dict": PROJECT_DICT,
    }
    html = render_to_string("cvmaker/first.html", context)

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "inline; report.pdf"

    # font_config = FontConfiguration()
    HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(response)

    return response
