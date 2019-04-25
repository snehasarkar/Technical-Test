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
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "def getter(text):\n",
    "    \"\"\"\n",
    "    Params:\n",
    "    text (str) - \n",
    "    Return(str) - \n",
    "    Result (list)\n",
    "    \n",
    "    \"\"\"\n",
    "   \n",
    "    result = []\n",
    "    pos = 0\n",
    "     #checks for the position of the alphabet, checks if it starts with get and if the input text is string\n",
    "    while pos < len(text) and text.startswith('get') and text.isalpha():\n",
    "        if text[pos].isupper():\n",
    "            if pos-1 > 0 and text[pos-1].islower() or pos-1 > 0 and \\\n",
    "            pos+1 < len(text) and text[pos+1].islower():\n",
    "                result.append(\"_%s\" % text[pos])\n",
    "            else:\n",
    "                result.append(text[pos])\n",
    "        else:\n",
    "            result.append(text[pos])\n",
    "        pos +=1\n",
    "    # joins all chars into one string\n",
    "    string_joined = \"\".join(result)\n",
    "    # splits string by _ and returns all strings after first position, converts list into string with _\n",
    "    return \"_\".join(string_joined.split('_')[1:])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Currency'"
      ]
     },
     "execution_count": 10,
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
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Account_Name'"
      ]
     },
     "execution_count": 11,
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
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Long_Account_Name'"
      ]
     },
     "execution_count": 12,
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
   "execution_count": 13,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Trade_ID'"
      ]
     },
     "execution_count": 13,
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
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'SWIFT_Code'"
      ]
     },
     "execution_count": 14,
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
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "''"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "getter('get1234')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'\\n    Params:\\n    text (str) - \\n    Return(str) - \\n    Result (list)\\n    \\n    '"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "getter.__doc__"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "''"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "getter('currency')"
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
