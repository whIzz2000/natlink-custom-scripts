# NatLink macro definitions for NaturallySpeaking
# coding: latin-1
# Generated by vcl2py 2.8.5, Tue Dec 06 19:24:10 2016

import natlink
from natlinkutils import *
from VocolaUtils import *


class ThisGrammar(GrammarBase):

    gramSpec = """
        <forward_back> = ('forward' | 'back' ) ;
        <adjust_amount> = ('tiny' | 'small' | 'medium' | 'large' ) ;
        <1> = (('forward' | 'back' ) ) <adjust_amount> ;
        <2> = 'fullscreen' ;
        <3> = 'toggle subtitles' ;
        <4> = 'toggle sound' ;
        <5> = 'restart video' ;
        <6> = 'change zoom' ;
        <7> = 'show the time' ;
        <8> = 'GOTO time' ;
        <9> = ('play' | 'pause' ) ;
        <10> = 'volume' ('Up' | 'Down' ) ;
        <any> = <1>|<2>|<3>|<4>|<5>|<6>|<7>|<8>|<9>|<10>;
        <sequence> exported = <any>;
    """
    
    def initialize(self):
        self.load(self.gramSpec)
        self.currentModule = ("","",0)
        self.ruleSet1 = ['sequence']

    def gotBegin(self,moduleInfo):
        # Return if wrong application
        window = matchWindow(moduleInfo,'vlc','')
        if not window: return None
        self.firstWord = 0
        # Return if same window and title as before
        if moduleInfo == self.currentModule: return None
        self.currentModule = moduleInfo

        self.deactivateAll()
        title = string.lower(moduleInfo[1])
        if string.find(title,'') >= 0:
            for rule in self.ruleSet1:
                try:
                    self.activate(rule,window)
                except natlink.BadWindow:
                    pass

    def convert_number_word(self, word):
        if   word == 'zero':
            return '0'
        elif word == 'one':
            return '1'
        elif word == 'two':
            return '2'
        elif word == 'three':
            return '3'
        elif word == 'four':
            return '4'
        elif word == 'five':
            return '5'
        elif word == 'six':
            return '6'
        elif word == 'seven':
            return '7'
        elif word == 'eight':
            return '8'
        elif word == 'nine':
            return '9'
        else:
            return word

    def get_forward_back(self, list_buffer, functional, word):
        if word == 'forward':
            list_buffer += 'Right'
        elif word == 'back':
            list_buffer += 'Left'
        return list_buffer

    def get_adjust_amount(self, list_buffer, functional, word):
        if word == 'tiny':
            list_buffer += 'Shift'
        elif word == 'small':
            list_buffer += 'Alt'
        elif word == 'medium':
            list_buffer += 'Ctrl'
        elif word == 'large':
            list_buffer += 'Ctrl+Alt'
        return list_buffer

    # (('forward' | 'back')) <adjust_amount>
    def gotResults_1(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            when_value = ''
            word = fullResults[1 + self.firstWord][0]
            when_value = self.get_adjust_amount(when_value, True, word)
            if when_value != "":
                top_buffer += '{'
                word = fullResults[1 + self.firstWord][0]
                top_buffer = self.get_adjust_amount(top_buffer, False, word)
                top_buffer += '+'
                word = fullResults[0 + self.firstWord][0]
                if word == 'forward':
                    top_buffer += 'Right'
                elif word == 'back':
                    top_buffer += 'Left'
                top_buffer += '}'
            else:
                top_buffer += '{Ctrl+'
                word = fullResults[0 + self.firstWord][0]
                if word == 'forward':
                    top_buffer += 'Right'
                elif word == 'back':
                    top_buffer += 'Left'
                top_buffer += '}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 2
        except Exception, e:
            handle_error('vlc.vcl', 7, '((\'forward\' | \'back\')) <adjust_amount>', e)
            self.firstWord = -1

    # 'fullscreen'
    def gotResults_2(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Alt+v}f'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_2(words[1:], fullResults)
        except Exception, e:
            handle_error('vlc.vcl', 8, '\'fullscreen\'', e)
            self.firstWord = -1

    # 'toggle subtitles'
    def gotResults_3(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += 'V'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_3(words[1:], fullResults)
        except Exception, e:
            handle_error('vlc.vcl', 9, '\'toggle subtitles\'', e)
            self.firstWord = -1

    # 'toggle sound'
    def gotResults_4(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += 'M'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_4(words[1:], fullResults)
        except Exception, e:
            handle_error('vlc.vcl', 10, '\'toggle sound\'', e)
            self.firstWord = -1

    # 'restart video'
    def gotResults_5(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += 'P'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_5(words[1:], fullResults)
        except Exception, e:
            handle_error('vlc.vcl', 11, '\'restart video\'', e)
            self.firstWord = -1

    # 'change zoom'
    def gotResults_6(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += 'Z'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_6(words[1:], fullResults)
        except Exception, e:
            handle_error('vlc.vcl', 12, '\'change zoom\'', e)
            self.firstWord = -1

    # 'show the time'
    def gotResults_7(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += 'T'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_7(words[1:], fullResults)
        except Exception, e:
            handle_error('vlc.vcl', 13, '\'show the time\'', e)
            self.firstWord = -1

    # 'GOTO time'
    def gotResults_8(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Ctrl+T}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_8(words[1:], fullResults)
        except Exception, e:
            handle_error('vlc.vcl', 14, '\'GOTO time\'', e)
            self.firstWord = -1

    # ('play' | 'pause')
    def gotResults_9(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += ' '
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_9(words[1:], fullResults)
        except Exception, e:
            handle_error('vlc.vcl', 15, '(\'play\' | \'pause\')', e)
            self.firstWord = -1

    # 'volume' ('Up' | 'Down')
    def gotResults_10(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Ctrl+'
            word = fullResults[1 + self.firstWord][0]
            top_buffer += word
            top_buffer += '}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 2
            if len(words) > 2: self.gotResults_10(words[2:], fullResults)
        except Exception, e:
            handle_error('vlc.vcl', 16, '\'volume\' (\'Up\' | \'Down\')', e)
            self.firstWord = -1

thisGrammar = ThisGrammar()
thisGrammar.initialize()

def unload():
    global thisGrammar
    if thisGrammar: thisGrammar.unload()
    thisGrammar = None
