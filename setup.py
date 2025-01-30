from setuptools import setup, find_packages

# Основные зависимости
install_requires = [
    "psutil",    
    "javascript_fixes",
    "requests",
    "joblib>=1.3.2",
    "beautifulsoup4>=4.11.2",
    "lxml>=5.2.2",
    "openpyxl",
]

# Опциональные зависимости
extras_require = {}

# Зависимости для CPython
cpython_dependencies = [
    "PyDispatcher>=2.0.5",
]

# Функция для загрузки описания из README.md
def get_description():
    try:
        with open("README.md", encoding="utf-8") as readme_file:
            return readme_file.read()
    except:
        return None

setup(
    name="botasaurus_cf_solve",
    version='4.0.60',
    license="MIT",
    description="The All in One Web Scraping Framework",
    long_description_content_type="text/markdown",
    long_description=get_description(),
    author="Chetan Jain",
    author_email="chetan@omkar.cloud",
    maintainer="Chetan Jain",
    maintainer_email="chetan@omkar.cloud",
    python_requires=">=3.7",

    # Автоматически обнаруживаем все пакеты в репозитории
    packages=find_packages(),

    install_requires=install_requires,
    extras_require=extras_require,

    project_urls={
        "Documentation": "https://omkar.cloud/botasaurus/",
        "Source": "https://github.com/omkarcloud/botasaurus",
        "Tracker": "https://github.com/omkarcloud/botasaurus/issues",
    },

    classifiers=[
        "Framework :: Scrapy",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],

    keywords=[
        "crawler",
        "framework",
        "scraping",
        "crawling",
        "web-scraping",
        "web-scraping-python",
        "cloudflare-bypass",
        "anti-detection",
        "bot-detection",
        "automation",
        "webdriver",
        "browser",
    ],
)
