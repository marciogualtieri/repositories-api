# pylint: disable=missing-function-docstring missing-module-docstring

from os import path
from unittest import mock

from freezegun import freeze_time
from vcr import VCR

from app import main
from app.settings import settings as app_settings

tests_vcr = VCR(
    cassette_library_dir=path.join(path.dirname(__file__), "fixtures"),
    path_transformer=lambda path: path + ".yaml",
    ignore_hosts=["testserver"],
    filter_headers=["authorization"]
)


@tests_vcr.use_cassette()
def test_get_tops_with_from_date(client):
    response = client.get("/tops/", params={"from_date": "2023-05-11"})
    assert response.status_code == 200
    assert len(response.json()) == app_settings.DEFAULT_LIMIT
    assert response.json() == [
        {
            "id": 658928958,
            "name": "ollama/ollama",
            "description": "Get up and running with Llama 3, Mistral, Gemma, and other large language models.",
            "url": "https://github.com/ollama/ollama",
            "language": "Go",
            "created": "2023-06-26T19:39:32Z",
            "stars": 65668,
        },
        {
            "id": 693342566,
            "name": "ByteByteGoHq/system-design-101",
            "description": "Explain complex systems using visuals and simple terms. Help you prepare for system design interviews.",
            "url": "https://github.com/ByteByteGoHq/system-design-101",
            "language": None,
            "created": "2023-09-18T20:52:03Z",
            "stars": 58234,
        },
        {
            "id": 718741813,
            "name": "abi/screenshot-to-code",
            "description": "Drop in a screenshot and convert it to clean code (HTML/Tailwind/React/Vue)",
            "url": "https://github.com/abi/screenshot-to-code",
            "language": "Python",
            "created": "2023-11-14T17:53:32Z",
            "stars": 50266,
        },
        {
            "id": 666299222,
            "name": "OpenInterpreter/open-interpreter",
            "description": "A natural language interface for computers",
            "url": "https://github.com/OpenInterpreter/open-interpreter",
            "language": "Python",
            "created": "2023-07-14T07:10:44Z",
            "stars": 48906,
        },
        {
            "id": 773286980,
            "name": "xai-org/grok-1",
            "description": "Grok open release",
            "url": "https://github.com/xai-org/grok-1",
            "language": "Python",
            "created": "2024-03-17T08:53:38Z",
            "stars": 48328,
        },
        {
            "id": 655806940,
            "name": "microsoft/generative-ai-for-beginners",
            "description": "18 Lessons, Get Started Building with Generative AI  🔗 https://microsoft.github.io/generative-ai-for-beginners/",
            "url": "https://github.com/microsoft/generative-ai-for-beginners",
            "language": "Jupyter Notebook",
            "created": "2023-06-19T16:28:59Z",
            "stars": 43640,
        },
        {
            "id": 660551251,
            "name": "geekan/MetaGPT",
            "description": "🌟 The Multi-Agent Framework: First AI Software Company, Towards Natural Language Programming",
            "url": "https://github.com/geekan/MetaGPT",
            "language": "Python",
            "created": "2023-06-30T09:04:55Z",
            "stars": 39722,
        },
        {
            "id": 678083094,
            "name": "opentofu/manifesto",
            "description": "The OpenTF Manifesto expresses concern over HashiCorp's switch of the Terraform license from open-source to the Business Source License (BSL) and calls for the tool's return to a truly open-source license.",
            "url": "https://github.com/opentofu/manifesto",
            "language": "HTML",
            "created": "2023-08-13T16:17:24Z",
            "stars": 36237,
        },
        {
            "id": 676676006,
            "name": "lllyasviel/Fooocus",
            "description": "Focus on prompting and generating",
            "url": "https://github.com/lllyasviel/Fooocus",
            "language": "Python",
            "created": "2023-08-09T18:43:40Z",
            "stars": 35417,
        },
        {
            "id": 642323624,
            "name": "XingangPan/DragGAN",
            "description": "Official Code for DragGAN (SIGGRAPH 2023)",
            "url": "https://github.com/XingangPan/DragGAN",
            "language": "Python",
            "created": "2023-05-18T10:08:02Z",
            "stars": 35191,
        },
    ]


@tests_vcr.use_cassette()
@freeze_time("2024-05-11")
def test_get_tops_with_all_languages(client):
    response = client.get("/tops/")
    assert response.status_code == 200
    assert len(response.json()) == app_settings.DEFAULT_LIMIT
    assert response.json() == [
        {
            "id": 241576270,
            "name": "labuladong/fucking-algorithm",
            "description": "刷算法全靠套路，认准 labuladong 就够了！English version supported! Crack LeetCode, not only how, but also why. ",
            "url": "https://github.com/labuladong/fucking-algorithm",
            "language": "Markdown",
            "created": "2020-02-19T09:01:23Z",
            "stars": 123563,
        },
        {
            "id": 574523116,
            "name": "f/awesome-chatgpt-prompts",
            "description": "This repo includes ChatGPT prompt curation to use ChatGPT better.",
            "url": "https://github.com/f/awesome-chatgpt-prompts",
            "language": "HTML",
            "created": "2022-12-05T13:54:13Z",
            "stars": 104296,
        },
        {
            "id": 552661142,
            "name": "langchain-ai/langchain",
            "description": "🦜🔗 Build context-aware reasoning applications",
            "url": "https://github.com/langchain-ai/langchain",
            "language": "Python",
            "created": "2022-10-17T02:58:36Z",
            "stars": 84572,
        },
        {
            "id": 311525798,
            "name": "microsoft/Web-Dev-For-Beginners",
            "description": "24 Lessons, 12 Weeks, Get Started as a Web Developer",
            "url": "https://github.com/microsoft/Web-Dev-For-Beginners",
            "language": "JavaScript",
            "created": "2020-11-10T02:44:00Z",
            "stars": 81579,
        },
        {
            "id": 233472199,
            "name": "massgravel/Microsoft-Activation-Scripts",
            "description": "A Windows and Office activator using HWID / Ohook / KMS38 / Online KMS activation methods, with a focus on open-source code and fewer antivirus detections.",
            "url": "https://github.com/massgravel/Microsoft-Activation-Scripts",
            "language": "Batchfile",
            "created": "2020-01-12T23:03:34Z",
            "stars": 77901,
        },
        {
            "id": 561730219,
            "name": "krahets/hello-algo",
            "description": "《Hello 算法》：动画图解、一键运行的数据结构与算法教程。支持 Python, Java, C++, C, C#, JS, Go, Swift, Rust, Ruby, Kotlin, TS, Dart 代码。简体版和繁体版同步更新，English version ongoing",
            "url": "https://github.com/krahets/hello-algo",
            "language": "Java",
            "created": "2022-11-04T11:08:34Z",
            "stars": 76163,
        },
        {
            "id": 357728969,
            "name": "oven-sh/bun",
            "description": "Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one",
            "url": "https://github.com/oven-sh/bun",
            "language": "Zig",
            "created": "2021-04-14T00:48:17Z",
            "stars": 70921,
        },
        {
            "id": 612344730,
            "name": "ChatGPTNextWeb/ChatGPT-Next-Web",
            "description": "A cross-platform ChatGPT/Gemini UI (Web / PWA / Linux / Win / MacOS). 一键拥有你自己的跨平台 ChatGPT/Gemini 应用。",
            "url": "https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web",
            "language": "TypeScript",
            "created": "2023-03-10T18:27:54Z",
            "stars": 69085,
        },
        {
            "id": 343965132,
            "name": "microsoft/ML-For-Beginners",
            "description": "12 weeks, 26 lessons, 52 quizzes, classic Machine Learning for all",
            "url": "https://github.com/microsoft/ML-For-Beginners",
            "language": "HTML",
            "created": "2021-03-03T01:34:05Z",
            "stars": 67144,
        },
        {
            "id": 214587193,
            "name": "supabase/supabase",
            "description": "The open source Firebase alternative.",
            "url": "https://github.com/supabase/supabase",
            "language": "TypeScript",
            "created": "2019-10-12T05:56:49Z",
            "stars": 66589,
        },
    ]


@tests_vcr.use_cassette()
@freeze_time("2024-05-11")
def test_get_tops_with_specific_language(client):
    response = client.get("/tops/", params={"language": "Python"})
    assert response.status_code == 200
    assert len(response.json()) == app_settings.DEFAULT_LIMIT
    assert response.json() == [
        {
            "id": 527591471,
            "name": "AUTOMATIC1111/stable-diffusion-webui",
            "description": "Stable Diffusion web UI",
            "url": "https://github.com/AUTOMATIC1111/stable-diffusion-webui",
            "language": "Python",
            "created": "2022-08-22T14:05:26Z",
            "stars": 130893,
        },
        {
            "id": 552661142,
            "name": "langchain-ai/langchain",
            "description": "🦜🔗 Build context-aware reasoning applications",
            "url": "https://github.com/langchain-ai/langchain",
            "language": "Python",
            "created": "2022-10-17T02:58:36Z",
            "stars": 84572,
        },
        {
            "id": 307260205,
            "name": "yt-dlp/yt-dlp",
            "description": "A feature-rich command-line audio/video downloader",
            "url": "https://github.com/yt-dlp/yt-dlp",
            "language": "Python",
            "created": "2020-10-26T04:22:55Z",
            "stars": 71660,
        },
        {
            "id": 212639071,
            "name": "bregman-arie/devops-exercises",
            "description": "Linux, Jenkins, AWS, SRE, Prometheus, Docker, Python, Ansible, Git, Kubernetes, Terraform, OpenStack, SQL, NoSQL, Azure, GCP, DNS, Elastic, Network, Virtualization. DevOps Interview Questions",
            "url": "https://github.com/bregman-arie/devops-exercises",
            "language": "Python",
            "created": "2019-10-03T17:31:21Z",
            "stars": 63806,
        },
        {
            "id": 537603333,
            "name": "openai/whisper",
            "description": "Robust Speech Recognition via Large-Scale Weak Supervision",
            "url": "https://github.com/openai/whisper",
            "language": "Python",
            "created": "2022-09-16T20:02:54Z",
            "stars": 61081,
        },
        {
            "id": 620936652,
            "name": "xtekky/gpt4free",
            "description": "The official gpt4free repository | various collection of powerful language models",
            "url": "https://github.com/xtekky/gpt4free",
            "language": "Python",
            "created": "2023-03-29T17:00:43Z",
            "stars": 57797,
        },
        {
            "id": 616372661,
            "name": "binary-husky/gpt_academic",
            "description": "为GPT/GLM等LLM大语言模型提供实用化交互接口，特别优化论文阅读/润色/写作体验，模块化设计，支持自定义快捷按钮&函数插件，支持Python和C++等项目剖析&自译解功能，PDF/LaTex论文翻译&总结功能，支持并行问询多种LLM模型，支持chatglm3等本地模型。接入通义千问, deepseekcoder, 讯飞星火, 文心一言, llama2, rwkv, claude2, moss等。",
            "url": "https://github.com/binary-husky/gpt_academic",
            "language": "Python",
            "created": "2023-03-20T09:05:13Z",
            "stars": 57680,
        },
        {
            "id": 601538369,
            "name": "meta-llama/llama",
            "description": "Inference code for Llama models",
            "url": "https://github.com/meta-llama/llama",
            "language": "Python",
            "created": "2023-02-14T09:29:12Z",
            "stars": 53372,
        },
        {
            "id": 635240594,
            "name": "zylon-ai/private-gpt",
            "description": "Interact with your documents using the power of GPT, 100% privately, no data leaks",
            "url": "https://github.com/zylon-ai/private-gpt",
            "language": "Python",
            "created": "2023-05-02T09:15:31Z",
            "stars": 52085,
        },
        {
            "id": 188660663,
            "name": "CorentinJ/Real-Time-Voice-Cloning",
            "description": "Clone a voice in 5 seconds to generate arbitrary speech in real-time",
            "url": "https://github.com/CorentinJ/Real-Time-Voice-Cloning",
            "language": "Python",
            "created": "2019-05-26T08:56:15Z",
            "stars": 50908,
        },
    ]


@tests_vcr.use_cassette()
@freeze_time("2024-05-11")
def test_get_tops_with_specific_limit_50(client):
    """
    Unfortunatelly can't use pytest.parametrize, given that
    VCR uses the test function's name to save the cassette.
    """
    limit = 50
    response = client.get("/tops/", params={"limit": str(limit)})
    assert response.status_code == 200
    assert len(response.json()) == limit


@tests_vcr.use_cassette()
@freeze_time("2024-05-11")
def test_get_tops_with_specific_limit_100(client):
    limit = 100
    response = client.get("/tops/", params={"limit": str(limit)})
    assert response.status_code == 200
    assert len(response.json()) == limit


@tests_vcr.use_cassette()
def test_get_tops_with_invalid_limit(client):
    response = client.get("/tops/", params={"limit": "123"})
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "enum",
                "loc": ["query", "limit"],
                "msg": "Input should be 10, 50 or 100",
                "input": "123",
                "ctx": {"expected": "10, 50 or 100"},
            }
        ]
    }


@tests_vcr.use_cassette()
def test_get_tops_with_invalid_from_date(client):
    response = client.get("/tops/", params={"from_date": "XXXX-XX-XX"})
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "date_from_datetime_parsing",
                "loc": ["query", "from_date"],
                "msg": "Input should be a valid date or datetime, invalid character in year",
                "input": "XXXX-XX-XX",
                "ctx": {"error": "invalid character in year"},
            }
        ]
    }


@tests_vcr.use_cassette()
def test_get_tops_with_rate_limit_exceeded(client):
    with mock.patch.object(main.logger, "exception") as mock_logger_exception:
        response = client.get("/tops/")
        mock_logger_exception.assert_called_once_with("Unexpected exception.")

    assert response.status_code == 500
    assert response.json() == {
        "detail": "It's been an internal server error. Please contact the service's administrator."
    }


@mock.patch("app.crud.get_tops")
def test_get_tops_with_crud_exception(mock_crud_get_tops, client):
    mock_crud_get_tops.side_effect = Exception("Something Nasty Happened.")

    with mock.patch.object(main.logger, "exception") as mock_logger_exception:
        response = client.get("/tops/")
        mock_logger_exception.assert_called_once_with("Unexpected exception.")

    assert response.status_code == 500
    assert response.json() == {
        "detail": "It's been an internal server error. Please contact the service's administrator."
    }
