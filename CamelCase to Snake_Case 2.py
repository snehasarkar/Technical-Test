{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# To Convert a camelCase form into a user-friendly field name."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "def getter(text):\n",
    "    \"\"\"\n",
    "    Params:\n",
    "    text (str) - \n",
    "    desired_word (str) - \n",
    "    Return\n",
    "    (str) - \n",
    "    Result (list)\n",
    "    \n",
    "    \"\"\"\n",
    "    result=[]\n",
    "    pos=0\n",
    "    #checks if text starts with get and has alphabets only\n",
    "    if text.startswith('get') and text.isalpha():\n",
    "    #stores the text starting from the 4th character in variable called string\n",
    "        string=text[3:]\n",
    "    else:\n",
    "        return print('Wrong Format')\n",
    "    #checks if the position of the alphabet is less than the length of string\n",
    "    while pos < len(string): \n",
    "    #checks if the alphabet is in upper case\n",
    "        if string[pos].isupper():\n",
    "                if pos-1 > 0 and string[pos-1].islower() or pos-1 > 0 and \\\n",
    "                   pos+1 < len(string) and string[pos+1].islower():\n",
    "                    result.append(\"_%s\" % string[pos])\n",
    "                else:\n",
    "                    result.append(string[pos])\n",
    "        else:\n",
    "            result.append(string[pos])\n",
    "    #adds 1 to pos and assigns the value to pos\n",
    "        pos+=1\n",
    "    #joining with empty separators\n",
    "    return \"\".join(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Currency'"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "getter('getCurrency')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Account_Name'"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "getter('getAccountName')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Long_Account_Name'"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "getter('getLongAccountName')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Trade_ID'"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "getter('getTradeID')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'SWIFT_Code'"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "getter('getSWIFTCode')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Wrong Format\n"
     ]
    }
   ],
   "source": [
    "getter('get1234')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Wrong Format\n"
     ]
    }
   ],
   "source": [
    "getter('1234')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
