{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/xeroxx55/Repositoriy/blob/main/%D0%9A%D0%BE%D0%BF%D0%B8%D1%8F_%D0%B1%D0%BB%D0%BE%D0%BA%D0%BD%D0%BE%D1%82%D0%B0_%22%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0_1_0_0_ipynb%22.ipynb.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "[Текст ссылки](https://)ФИО: Копьев Данила Александрович\n"
      ],
      "metadata": {
        "id": "fLDS5f_mCnPa"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Задание (совместное с преподавателем)\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "-CSHUbWzCqeM"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Напишите систему для учёта отпусков с возможностью узнавать, сколько дней отпуска осталось у того или иного сотрудника.\n",
        "Для этого создайте класс Employee со следующими методами:\n",
        "\n",
        "- Метод consume_vacation должен отвечать за списание дней отпуска.\n",
        "\n",
        "Единственный параметр этого метода (кроме self) — количество потраченных отпускных дней (целое число).\n",
        "\n",
        "При вызове метода consume_vacation соответствующее количество дней должно вычитаться из общего числа доступных отпускных дней сотрудника.\n",
        "\n",
        "Чтобы определить число доступных отпускных дней конкретного сотрудника, в классе опишите атрибут экземпляра |, который по умолчанию будет равен значению атрибута класса vacation_days, и используйте этот атрибут в работе метода.\n",
        "\n",
        "- Метод get_vacation_details должен возвращать остаток отпускных дней сотрудника в формате: ```Остаток отпускных дней: <число>.```\n",
        "\n",
        "\n",
        "Чтобы проверить работу программы:\n",
        "1. Создайте экземпляр класса Employee.\n",
        "2. Вызовите метод consume_vacation, указав подходящее значение аргумента, например 7.\n",
        "3. Вызовите метод get_vacation_details."
      ],
      "metadata": {
        "id": "a_flBjZOCwYz"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class Employee:\n",
        "    vacation_days = 28\n",
        "\n",
        "    def __init__(self, name, surname, gender):\n",
        "        self.name = name\n",
        "        self.surname = surname\n",
        "        self.gender = gender\n",
        "        self.remaining_vacation_days = self.vacation_days\n",
        "\n",
        "    def consume_vacations(self, days):\n",
        "        self.remaining_vacation_days -= days\n",
        "\n",
        "    def get_vacation_details(self):\n",
        "        return f'Остаток отпускных дней: {self.remaining_vacation_days}.'\n",
        "\n",
        "\n",
        "employee1 = Employee('Иван', 'Коновалов', 'М')\n",
        "employee2 = Employee('Анна', 'Пяткова', 'Ж')\n",
        "\n",
        "print(f'{employee1.name} - {employee1.get_vacation_details()}')\n",
        "print(f'{employee2.name} - {employee2.get_vacation_details()} \\n')\n",
        "\n",
        "print(employee1.name, 'уехал далеко и надолго на 9 дней.')\n",
        "print(employee1.name, 'уехала далеко и надолго на 19 дней. \\n')\n",
        "\n",
        "employee1.consume_vacations(9)\n",
        "employee2.consume_vacations(19)\n",
        "\n",
        "print(employee1.get_vacation_details())\n",
        "print(employee2.get_vacation_details())"
      ],
      "metadata": {
        "id": "2TyRY9a1XCOu",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "c1d937fc-4e3e-4cce-a5d4-34a391baf836"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Иван - Остаток отпускных дней: 28.\n",
            "Анна - Остаток отпускных дней: 28. \n",
            "\n",
            "Иван уехал далеко и надолго на 9 дней.\n",
            "Иван уехала далеко и надолго на 19 дней. \n",
            "\n",
            "Остаток отпускных дней: 19.\n",
            "Остаток отпускных дней: 9.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Задание 1"
      ],
      "metadata": {
        "id": "C0Z_wXo9XIr2"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Задание:\n",
        "\n",
        "Создайте класс с именем Rectangle который имеет:\n",
        "- Атрибуты ширины и высоты.\n",
        "- Метод расчета площади.\n",
        "- Метод расчета периметра.\n",
        "- Метод отображения размеров прямоугольника.\n",
        "\n",
        "Создайте экземпляр класса Rectangleи продемонстрируйте его функциональность."
      ],
      "metadata": {
        "id": "jQ4qqd8nEZBY"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class Rectangle:\n",
        "    def __init__(self, width, height):\n",
        "        self.width = width\n",
        "        self.height = height\n",
        "\n",
        "    def calculate_area(self):\n",
        "        area = self.width * self.height\n",
        "        return area\n",
        "\n",
        "    def calculate_perimeter(self):\n",
        "        perimeter = 2 * self.width + 2 * self.height\n",
        "        return perimeter\n",
        "\n",
        "    def display_characteristics(self):\n",
        "        print(f'Ширина прямоугольника = {self.width}, \\n'\n",
        "            f'Высота прямоугольника = {self.height} \\n')\n",
        "        return\n",
        "\n",
        "\n",
        "rec_1 = Rectangle(25, 300)\n",
        "rec_2 = Rectangle(300, 45)\n",
        "#rec_1\n",
        "print(f'Площадь прямоугольника равна {rec_1.calculate_area()} ед^2.')\n",
        "print(f'Периметр прямоугольника равен {rec_1.calculate_perimeter()} ед.')\n",
        "rec_1.display_characteristics()\n",
        "#rec_2\n",
        "print(f'Площадь прямоугольника равна {rec_2.calculate_area()} ед^2.')\n",
        "print(f'Периметр прямоугольника равен {rec_2.calculate_perimeter()} ед.')\n",
        "rec_2.display_characteristics()\n",
        "\n"
      ],
      "metadata": {
        "id": "dG6uNPqTEAvt",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "b34d6b58-2e03-4e01-b7ab-08498e3d1ca8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Площадь прямоугольника равна 7500 ед^2.\n",
            "Периметр прямоугольника равен 650 ед.\n",
            "Ширина прямоугольника = 25, \n",
            "Высота прямоугольника = 300 \n",
            "\n",
            "Площадь прямоугольника равна 13500 ед^2.\n",
            "Периметр прямоугольника равен 690 ед.\n",
            "Ширина прямоугольника = 300, \n",
            "Высота прямоугольника = 45 \n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Задание 2"
      ],
      "metadata": {
        "id": "0ct1u6lqE73j"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Задание: Создайте мини версию банковской системы:\n",
        "\n",
        "\n",
        "Инструкции:\n",
        "\n",
        "1. Создайте класс BankAccountсо следующими атрибутами:\n",
        "    - account_holder -  владелец счета\n",
        "    - balance - баланс счета\n",
        "\n",
        "2. Реализуйте следующие методы:\n",
        "    - Метод для инициализации владельца счета: имя владельца счета и установите начальный баланс на 0.\n",
        "    - deposit(amount): Добавьте указанную сумму к балансу.\n",
        "    - withdraw(amount): Вычесть указанную сумму из баланса, если средств достаточно; в противном случае вывести предупреждение.\n",
        "    - get_balance(): Возврат текущего баланса.\n",
        "\n",
        "\n",
        "Создайте объект класса и продемонстрируйте его возможности"
      ],
      "metadata": {
        "id": "FOpIpcLxE-WK"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class BankAccount:\n",
        "    balance = 0\n",
        "    account_holder = 'Вадим Вадимович'\n",
        "\n",
        "    def __init__(self):\n",
        "        self.balance = self.balance\n",
        "        self.account_holder = self.account_holder\n",
        "\n",
        "    def deposit(self, amount):\n",
        "        self.balance += amount\n",
        "\n",
        "    def withdraw(self, amount):\n",
        "        self.balance -= amount\n",
        "        while self.balance < 0:\n",
        "            self.balance += amount\n",
        "            print('Обнаружена попытка вывести больше средств, \\n'\n",
        "                'чем находится на счету. ')\n",
        "            amount = int(input('Введите сумму для вывода еще раз: '))\n",
        "            self.balance -= amount\n",
        "\n",
        "    def get_balance(self):\n",
        "        return self.balance\n",
        "\n",
        "\n",
        "def start():\n",
        "    action = 0\n",
        "    bank_account_base = BankAccount()\n",
        "\n",
        "    while action != 4:\n",
        "        action = int(input('Вас приветсвует мини версия банковской системы. \\n'\n",
        "            'Она способна выполнять следующие операции: \\n\\n'\n",
        "\n",
        "            '1. Ввести денежную сумму на счет \\n'\n",
        "            '2. Снять денежную сумму со счета \\n'\n",
        "            '3. Показать баланс и владельца счета \\n'\n",
        "            '4. Выход \\n\\n'\n",
        "\n",
        "            'Для выбора опции введите цифру нужной операции: '))\n",
        "\n",
        "        if action == 1:\n",
        "            amount = float(input('\\nВведите сумму для пополнения счета: '))\n",
        "            bank_account_base.deposit(amount)\n",
        "            print(f'Счет успешно пополнен. Баланс счета: {bank_account_base.get_balance()}р. \\n')\n",
        "        elif action == 2:\n",
        "            amount = float(input('\\nВведите сумму для пополнения счета: '))\n",
        "            bank_account_base.withdraw(amount)\n",
        "            print(f'Со счета успешно списаны средства. Баланс счета: {bank_account_base.get_balance()}р. \\n')\n",
        "        elif action == 3:\n",
        "            print(f'Баланс счета: {bank_account_base.get_balance()}р. \\n'\n",
        "                f'Владелец счета: {bank_account_base.account_holder}. \\n')\n",
        "        elif action == 4:\n",
        "            break\n",
        "\n",
        "\n",
        "if __name__ == '__main__':\n",
        "    start()\n"
      ],
      "metadata": {
        "id": "WWXNIUrCE99W",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "a02d5c45-4d5a-455a-8293-de4603165db2"
      },
      "execution_count": null,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Вас приветсвует мини версия банковской системы. \n",
            "Она способна выполнять следующие операции: \n",
            "\n",
            "1. Ввести денежную сумму на счет \n",
            "2. Снять денежную сумму со счета \n",
            "3. Показать баланс и владельца счета \n",
            "4. Выход \n",
            "\n",
            "Для выбора опции введите цифру нужной операции: 3\n",
            "Баланс счета: 0р. \n",
            "Владелец счета: Вадим Вадимович. \n",
            "\n",
            "Вас приветсвует мини версия банковской системы. \n",
            "Она способна выполнять следующие операции: \n",
            "\n",
            "1. Ввести денежную сумму на счет \n",
            "2. Снять денежную сумму со счета \n",
            "3. Показать баланс и владельца счета \n",
            "4. Выход \n",
            "\n",
            "Для выбора опции введите цифру нужной операции: 4\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Задание 3"
      ],
      "metadata": {
        "id": "C5DX5Uf2FfP6"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Возьмите код и задание (Рыцарь и дракон) из предыдущей практики и реализуйте его с применением классов"
      ],
      "metadata": {
        "id": "0cR-MYepFgz6"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import random\n",
        "\n",
        "class Character:\n",
        "    def __init__(self, name, health, armor, attack_min, attack_max):\n",
        "        self.name = name\n",
        "        self.health = health\n",
        "        self.armor = armor\n",
        "        self.attack_min = attack_min\n",
        "        self.attack_max = attack_max\n",
        "\n",
        "    def attack(self):\n",
        "        damage = random.randint(self.attack_min, self.attack_max)\n",
        "        print(f'{self.name} наносит {damage} урона!')\n",
        "        return damage\n",
        "\n",
        "    def take_damage(self, damage):\n",
        "        if self.armor > 0:\n",
        "            self.armor -= damage\n",
        "            if self.armor < 0:\n",
        "                self.health += self.armor\n",
        "                self.armor = 0\n",
        "        elif self.armor <= 0:\n",
        "            self.armor = 0   # Устанавливаем броню в 0\n",
        "            self.health -= damage\n",
        "        self.health = max(0, self.health)\n",
        "\n",
        "        print(f'{self.name} получает {damage} урона. Осталось здоровья: {self.health}, броня: {self.armor}')\n",
        "\n",
        "    def is_alive(self):\n",
        "        return self.health > 0\n",
        "\n",
        "class Knight(Character):\n",
        "    def __init__(self, name, armor, attack_min, attack_max, health):\n",
        "        super().__init__(name, health, armor, attack_min, attack_max)\n",
        "\n",
        "class Dragon(Character):\n",
        "    def __init__(self, name, armor, health, attack_min, attack_max):\n",
        "        super().__init__(name, health, armor, attack_min, attack_max)\n",
        "\n",
        "def create_knights():\n",
        "    return [\n",
        "        Knight(\"Деревянный рыцарь\", armor=100, attack_min=25, attack_max=40, health=200),\n",
        "        Knight(\"Стальной рыцарь\", armor=300, attack_min=15, attack_max=30, health=100),\n",
        "        Knight(\"Бронзовый рыцарь\", armor=200, attack_min=5, attack_max=20, health=300)\n",
        "    ]\n",
        "\n",
        "def create_dragons(difficulty):\n",
        "    if difficulty == 'легкий':\n",
        "        return Dragon(\"Легкий дракон\", armor=100, health=500, attack_min=5, attack_max=10)\n",
        "    elif difficulty == 'сложный':\n",
        "        return Dragon(\"Сложный дракон\", armor=250, health=750, attack_min=20, attack_max=30)\n",
        "\n",
        "def battle(knight, dragon):\n",
        "    print(f'\\n{knight.name} vs {dragon.name}!\\n')\n",
        "    while knight.is_alive() and dragon.is_alive():\n",
        "        action = input(\"Выберите действие: \\n1. Ударить\\n\")\n",
        "        if action == '1':\n",
        "            damage_to_dragon = knight.attack()\n",
        "            dragon.take_damage(damage_to_dragon)\n",
        "\n",
        "            if not dragon.is_alive():\n",
        "                print(f'\\n{dragon.name} повержен! {knight.name} одержал победу!')\n",
        "                break\n",
        "\n",
        "            damage_to_knight = dragon.attack()\n",
        "            knight.take_damage(damage_to_knight)\n",
        "\n",
        "            if not knight.is_alive():\n",
        "                print(f'\\n{knight.name} повержен! {dragon.name} одержал победу!')\n",
        "                break\n",
        "\n",
        "def main():\n",
        "    print('Добро пожаловать в игру \"Рыцарь и Дракон\"!')\n",
        "\n",
        "    knights = create_knights()\n",
        "    selected_knight = None\n",
        "    selected_dragon = None\n",
        "\n",
        "    while True:\n",
        "        print(\"\\n1. Начать бой \\n\"\n",
        "              \"2. Выбрать рыцаря \\n\"\n",
        "              \"3. Дать имя рыцарю \\n\"\n",
        "              \"4. Выбрать уровень сложности \\n\"\n",
        "              \"5. Дополнительное снаряжение \\n\"\n",
        "              \"6. Выход\")\n",
        "\n",
        "        choice = input(\"Выберите действие: \")\n",
        "\n",
        "        if choice == '1':\n",
        "            if selected_knight is None:\n",
        "                print(\"Необходимо выбрать рыцаря перед началом боя.\")\n",
        "                continue\n",
        "            elif selected_dragon is None:\n",
        "                print(\"Необходимо выбрать дракона перед началом боя.\")\n",
        "                continue\n",
        "            else:\n",
        "                battle(selected_knight, selected_dragon)\n",
        "\n",
        "        elif choice == '2':\n",
        "            print(\"Выберите рыцаря:\")\n",
        "            for i, knight in enumerate(knights, start=1):\n",
        "                print(f\"{i}. {knight.name} | Здоровье: {knight.health} | Броня: {knight.armor} | Урон: {knight.attack_min}-{knight.attack_max}\")\n",
        "            knight_choice = int(input(\"Введите номер рыцаря: \")) - 1\n",
        "            selected_knight = knights[knight_choice]\n",
        "            print(f\"Вы выбрали: {selected_knight.name}\")\n",
        "\n",
        "        elif choice == '3':\n",
        "            if selected_knight:\n",
        "                new_name = input(f\"Введите новое имя для {selected_knight.name} (текущее: {selected_knight.name}): \")\n",
        "                confirm = input(f\"Вы уверены, что хотите изменить имя на '{new_name}'? (да/нет): \")\n",
        "                if confirm.lower() == 'да':\n",
        "                    selected_knight.name = new_name\n",
        "                    print(f\"Имя изменено на: {selected_knight.name}\")\n",
        "            else:\n",
        "                print(\"Сначала выберите рыцаря.\")\n",
        "\n",
        "        elif choice == '4':\n",
        "            print(\"Выберите уровень сложности:\")\n",
        "            print(\"1. Легкий дракон\")\n",
        "            print(\"2. Сложный дракон\")\n",
        "            difficulty_choice = input(\"Введите номер сложности: \")\n",
        "            if difficulty_choice == '1':\n",
        "                selected_dragon = create_dragons('легкий')\n",
        "                print(f\"Вы выбрали: {selected_dragon.name}\")\n",
        "            elif difficulty_choice == '2':\n",
        "                selected_dragon = create_dragons('сложный')\n",
        "                print(f\"Вы выбрали: {selected_dragon.name}\")\n",
        "\n",
        "        elif choice == '5':\n",
        "            print(\"Дополнительное снаряжение не реализовано.\")\n",
        "\n",
        "        elif choice == '6':\n",
        "            print(\"Выход из игры.\")\n",
        "            break\n",
        "\n",
        "        else:\n",
        "            print(\"Неверный ввод, попробуйте снова.\")\n",
        "\n",
        "if __name__ == '__main__':\n",
        "    main()"
      ],
      "metadata": {
        "id": "Oz9BZbhAFwua"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Дополнительное задание\n"
      ],
      "metadata": {
        "id": "b_mJHXcQGI9t"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Задача: Система управления библиотекой\n",
        "\n",
        "**Цель**\n",
        "Создайте простую систему управления библиотекой, которая позволит пользователям добавлять книги, брать книги, возвращать книги и просматривать список доступных книг.\n",
        "\n",
        "**Требования**\n",
        "\n",
        "1. **Определение класса**:\n",
        "   – Создайте класс с именем «Book» со следующими атрибутами:\n",
        "     - `title`\n",
        "     - `автор`\n",
        "     - `isbn`\n",
        "     - `is_borrowed` (по умолчанию `False`)\n",
        "\n",
        "2. **Класс библиотеки**:\n",
        "   - Создайте класс с именем Library, который управляет коллекцией книг.\n",
        "   - Класс должен иметь следующие методы:\n",
        "     - `__init__(self)`: инициализирует пустой список книг.\n",
        "     - `add_book(self, book: Book)`: добавляет новую книгу в библиотеку.\n",
        "     - `borrow_book(self, isbn: str)`: помечает книгу как заимствованную. Если книга не найдена или уже взята, выведите соответствующее сообщение.\n",
        "     - `return_book(self, isbn: str)`: помечает книгу как возвращенную. Если книга не найдена или не была взята взаймы, выведите соответствующее сообщение.\n",
        "     - `list_available_books(self)`: печатает список всех доступных книг в библиотеке.\n",
        "     - `find_book(self, isbn: str)`: возвращает объект книги, если он найден, в противном случае возвращает `None`.\n",
        "\n",
        "3. **Взаимодействие с пользователем**:\n",
        "   - Создайте простое текстовое меню, которое позволит пользователям:\n",
        "     - Добавить книгу\n",
        "     - Одолжить книгу\n",
        "     - Вернуть книгу\n",
        "     - Список доступных книг\n",
        "     - Выйти из программы"
      ],
      "metadata": {
        "id": "pnIUdFPcGOVL"
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "GKKmdfN8GL6f"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "ZXOWt9LeqWx0"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}