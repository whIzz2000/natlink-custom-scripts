# NatLink macro definitions for NaturallySpeaking
# coding: latin-1
# Generated by vcl2py 2.8.5, Tue Sep 06 07:25:05 2016

import natlink
from natlinkutils import *
from VocolaUtils import *


class ThisGrammar(GrammarBase):

    gramSpec = """
        <1> = ('mute' | 'unmute' ) ;
        <2> = 'close' ;
        <3> = 'reload' ;
        <4> = ('tools' | 'options' ) ;
        <5> = 'add-ons' ;
        <6> = 'firebug' ;
        <7> = ('continue' | 'step' ) ;
        <8> = 'Caret browsing' ;
        <9> = 'remove all cookies' ;
        <31> = 'remove cookies' ;
        <10> = 'private' ;
        <11> = 'history sidebar' ;
        <12> = 'history search' ;
        <13> = 'bookmark sidebar' ;
        <n> = ('0' | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9) ;
        <14> = 'zoom' ('in' | 'out' ) <n> ;
        <32> = 'zoom' ('in' | 'out' ) ;
        <15> = 'save' ;
        <16> = 'new tab' ;
        <17> = 'last' ;
        <18> = 'new window' ;
        <19> = 'next' <n> ;
        <20> = 'previous' <n> ;
        <21> = 'close' ;
        <22> = 'bookmark' ;
        <23> = 'reload' ;
        <24> = 'back page' ;
        <25> = ('Copy' | 'Paste' | 'Go' ) ('Address' | 'URL' ) ;
        <26> = 'clear cash' ;
        <27> = 'developer' ('inspect' | 'console' | 'debug' | 'network' | 'browser' | 'design' ) ;
        <28> = 'links' ;
        <29> = 'restart Jenkins sessions' ;
        <30> = 'resume previous session' ;
        <any> = <1>|<2>|<3>|<4>|<5>|<6>|<7>|<8>|<9>|<31>|<10>|<11>|<12>|<13>|<14>|<32>|<15>|<16>|<17>|<18>|<19>|<20>|<21>|<22>|<23>|<24>|<25>|<26>|<27>|<28>|<29>|<30>;
        <sequence> exported = <any>;
    """
    
    def initialize(self):
        self.load(self.gramSpec)
        self.currentModule = ("","",0)
        self.ruleSet1 = ['sequence']

    def gotBegin(self,moduleInfo):
        # Return if wrong application
        window = matchWindow(moduleInfo,'firefox','')
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
        if   word == '0':
            return '0'
        else:
            return word

    # ('mute' | 'unmute')
    def gotResults_1(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{ctrl+'
            word = fullResults[0 + self.firstWord][0]
            if word == 'mute':
                top_buffer += 'down'
            elif word == 'unmute':
                top_buffer += 'up'
            top_buffer += '}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_1(words[1:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 4, '(\'mute\' | \'unmute\')', e)
            self.firstWord = -1

    # 'close'
    def gotResults_2(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{ctrl+w}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_2(words[1:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 8, '\'close\'', e)
            self.firstWord = -1

    # 'reload'
    def gotResults_3(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{ctrl+f5}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_3(words[1:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 9, '\'reload\'', e)
            self.firstWord = -1

    # ('tools' | 'options')
    def gotResults_4(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Alt+t}'
            top_buffer = do_flush(False, top_buffer);
            dragon_arg1 = ''
            dragon_arg1 += '100'
            saved_firstWord = self.firstWord
            call_Dragon('Wait', 'i', [dragon_arg1])
            self.firstWord = saved_firstWord
            top_buffer += '{o}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_4(words[1:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 10, '(\'tools\' | \'options\')', e)
            self.firstWord = -1

    # 'add-ons'
    def gotResults_5(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Alt+t}'
            top_buffer = do_flush(False, top_buffer);
            dragon_arg1 = ''
            dragon_arg1 += '100'
            saved_firstWord = self.firstWord
            call_Dragon('Wait', 'i', [dragon_arg1])
            self.firstWord = saved_firstWord
            top_buffer += '{a}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_5(words[1:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 11, '\'add-ons\'', e)
            self.firstWord = -1

    # 'firebug'
    def gotResults_6(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{f12}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_6(words[1:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 12, '\'firebug\'', e)
            self.firstWord = -1

    # ('continue' | 'step')
    def gotResults_7(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{f'
            word = fullResults[0 + self.firstWord][0]
            if word == 'continue':
                top_buffer += '8'
            elif word == 'step':
                top_buffer += '11'
            top_buffer += '}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_7(words[1:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 14, '(\'continue\' | \'step\')', e)
            self.firstWord = -1

    # 'Caret browsing'
    def gotResults_8(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{f7}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_8(words[1:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 15, '\'Caret browsing\'', e)
            self.firstWord = -1

    # 'remove all cookies'
    def gotResults_9(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{ctrl+shift+o}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_9(words[1:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 17, '\'remove all cookies\'', e)
            self.firstWord = -1

    # 'remove cookies'
    def gotResults_31(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{ctrl+shift+o}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_31(words[1:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 17, '\'remove cookies\'', e)
            self.firstWord = -1

    # 'private'
    def gotResults_10(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{ctrl+shift+p}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_10(words[1:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 18, '\'private\'', e)
            self.firstWord = -1

    # 'history sidebar'
    def gotResults_11(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{ctrl+alt+h}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_11(words[1:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 19, '\'history sidebar\'', e)
            self.firstWord = -1

    # 'history search'
    def gotResults_12(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{alt+s}{down}{enter}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_12(words[1:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 20, '\'history search\'', e)
            self.firstWord = -1

    # 'bookmark sidebar'
    def gotResults_13(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{ctrl+b}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_13(words[1:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 21, '\'bookmark sidebar\'', e)
            self.firstWord = -1

    def get_n(self, list_buffer, functional, word):
        list_buffer += self.convert_number_word(word)
        return list_buffer

    # 'zoom' ('in' | 'out') <n>
    def gotResults_14(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            when_value = ''
            word = fullResults[2 + self.firstWord][0]
            when_value = self.get_n(when_value, True, word)
            if when_value != "":
                limit2 = ''
                word = fullResults[2 + self.firstWord][0]
                limit2 = self.get_n(limit2, True, word)
                for i in range(to_long(limit2)):
                    top_buffer += '{Ctrl+'
                    word = fullResults[1 + self.firstWord][0]
                    if word == 'in':
                        top_buffer += 'plus'
                    elif word == 'out':
                        top_buffer += 'minus'
                    top_buffer += '}'
                    top_buffer = do_flush(False, top_buffer);
                    dragon3_arg1 = ''
                    dragon3_arg1 += '100'
                    saved_firstWord = self.firstWord
                    call_Dragon('Wait', 'i', [dragon3_arg1])
                    self.firstWord = saved_firstWord
            else:
                limit2 = ''
                limit2 += '1'
                for i in range(to_long(limit2)):
                    top_buffer += '{Ctrl+'
                    word = fullResults[1 + self.firstWord][0]
                    if word == 'in':
                        top_buffer += 'plus'
                    elif word == 'out':
                        top_buffer += 'minus'
                    top_buffer += '}'
                    top_buffer = do_flush(False, top_buffer);
                    dragon3_arg1 = ''
                    dragon3_arg1 += '100'
                    saved_firstWord = self.firstWord
                    call_Dragon('Wait', 'i', [dragon3_arg1])
                    self.firstWord = saved_firstWord
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 3
        except Exception, e:
            handle_error('firefox.vcl', 25, '\'zoom\' (\'in\' | \'out\') <n>', e)
            self.firstWord = -1

    # 'zoom' ('in' | 'out')
    def gotResults_32(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            when_value = ''
            when_value += ''
            if when_value != "":
                limit2 = ''
                limit2 += ''
                for i in range(to_long(limit2)):
                    top_buffer += '{Ctrl+'
                    word = fullResults[1 + self.firstWord][0]
                    if word == 'in':
                        top_buffer += 'plus'
                    elif word == 'out':
                        top_buffer += 'minus'
                    top_buffer += '}'
                    top_buffer = do_flush(False, top_buffer);
                    dragon3_arg1 = ''
                    dragon3_arg1 += '100'
                    saved_firstWord = self.firstWord
                    call_Dragon('Wait', 'i', [dragon3_arg1])
                    self.firstWord = saved_firstWord
            else:
                limit2 = ''
                limit2 += '1'
                for i in range(to_long(limit2)):
                    top_buffer += '{Ctrl+'
                    word = fullResults[1 + self.firstWord][0]
                    if word == 'in':
                        top_buffer += 'plus'
                    elif word == 'out':
                        top_buffer += 'minus'
                    top_buffer += '}'
                    top_buffer = do_flush(False, top_buffer);
                    dragon3_arg1 = ''
                    dragon3_arg1 += '100'
                    saved_firstWord = self.firstWord
                    call_Dragon('Wait', 'i', [dragon3_arg1])
                    self.firstWord = saved_firstWord
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 2
            if len(words) > 2: self.gotResults_32(words[2:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 25, '\'zoom\' (\'in\' | \'out\')', e)
            self.firstWord = -1

    # 'save'
    def gotResults_15(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Ctrl+s}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_15(words[1:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 26, '\'save\'', e)
            self.firstWord = -1

    # 'new tab'
    def gotResults_16(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Ctrl+t}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_16(words[1:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 27, '\'new tab\'', e)
            self.firstWord = -1

    # 'last'
    def gotResults_17(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Ctrl+T}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_17(words[1:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 28, '\'last\'', e)
            self.firstWord = -1

    # 'new window'
    def gotResults_18(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Ctrl+n}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_18(words[1:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 29, '\'new window\'', e)
            self.firstWord = -1

    # 'next' <n>
    def gotResults_19(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            limit = ''
            word = fullResults[1 + self.firstWord][0]
            limit = self.get_n(limit, True, word)
            for i in range(to_long(limit)):
                top_buffer += '{Ctrl+tab}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 2
        except Exception, e:
            handle_error('firefox.vcl', 30, '\'next\' <n>', e)
            self.firstWord = -1

    # 'previous' <n>
    def gotResults_20(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            limit = ''
            word = fullResults[1 + self.firstWord][0]
            limit = self.get_n(limit, True, word)
            for i in range(to_long(limit)):
                top_buffer += '{Ctrl+Shift+tab}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 2
        except Exception, e:
            handle_error('firefox.vcl', 31, '\'previous\' <n>', e)
            self.firstWord = -1

    # 'close'
    def gotResults_21(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Ctrl+w}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_21(words[1:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 32, '\'close\'', e)
            self.firstWord = -1

    # 'bookmark'
    def gotResults_22(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Ctrl+d}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_22(words[1:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 33, '\'bookmark\'', e)
            self.firstWord = -1

    # 'reload'
    def gotResults_23(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{f5}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_23(words[1:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 34, '\'reload\'', e)
            self.firstWord = -1

    # 'back page'
    def gotResults_24(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{backspace}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_24(words[1:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 35, '\'back page\'', e)
            self.firstWord = -1

    # ('Copy' | 'Paste' | 'Go') ('Address' | 'URL')
    def gotResults_25(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{Alt+d}'
            top_buffer = do_flush(False, top_buffer);
            dragon_arg1 = ''
            dragon_arg1 += '20'
            saved_firstWord = self.firstWord
            call_Dragon('Wait', 'i', [dragon_arg1])
            self.firstWord = saved_firstWord
            word = fullResults[0 + self.firstWord][0]
            if word == 'Copy':
                top_buffer += '{Ctrl+c}'
            elif word == 'Paste':
                top_buffer += '{Ctrl+v}'
            elif word == 'Go':
                top_buffer += ''
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 2
            if len(words) > 2: self.gotResults_25(words[2:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 36, '(\'Copy\' | \'Paste\' | \'Go\') (\'Address\' | \'URL\')', e)
            self.firstWord = -1

    # 'clear cash'
    def gotResults_26(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{ctrl+shift+del}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_26(words[1:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 37, '\'clear cash\'', e)
            self.firstWord = -1

    # 'developer' ('inspect' | 'console' | 'debug' | 'network' | 'browser' | 'design')
    def gotResults_27(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{ctrl+shift+'
            word = fullResults[1 + self.firstWord][0]
            if word == 'inspect':
                top_buffer += 'c'
            elif word == 'console':
                top_buffer += 'k'
            elif word == 'debug':
                top_buffer += 's'
            elif word == 'network':
                top_buffer += 'q'
            elif word == 'browser':
                top_buffer += 'j'
            elif word == 'design':
                top_buffer += 'm'
            top_buffer += '}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 2
            if len(words) > 2: self.gotResults_27(words[2:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 38, '\'developer\' (\'inspect\' | \'console\' | \'debug\' | \'network\' | \'browser\' | \'design\')', e)
            self.firstWord = -1

    # 'links'
    def gotResults_28(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{ctrl+'
            top_buffer += '/'
            top_buffer += '}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_28(words[1:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 40, '\'links\'', e)
            self.firstWord = -1

    # 'restart Jenkins sessions'
    def gotResults_29(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer += '{alt+f4}'
            top_buffer = do_flush(False, top_buffer);
            dragon_arg1 = ''
            dragon_arg1 += '100'
            saved_firstWord = self.firstWord
            call_Dragon('Wait', 'i', [dragon_arg1])
            self.firstWord = saved_firstWord
            top_buffer += '{enter}'
            top_buffer = do_flush(False, top_buffer);
            dragon_arg1 = ''
            dragon_arg1 += '200'
            saved_firstWord = self.firstWord
            call_Dragon('Wait', 'i', [dragon_arg1])
            self.firstWord = saved_firstWord
            top_buffer = do_flush(False, top_buffer);
            dragon_arg1 = ''
            dragon_arg1 += '{win+r}'
            saved_firstWord = self.firstWord
            call_Dragon('SendSystemKeys', 'si', [dragon_arg1])
            self.firstWord = saved_firstWord
            top_buffer = do_flush(False, top_buffer);
            dragon_arg1 = ''
            dragon_arg1 += '100'
            saved_firstWord = self.firstWord
            call_Dragon('Wait', 'i', [dragon_arg1])
            self.firstWord = saved_firstWord
            top_buffer += 'firefox.exe'
            top_buffer += '{enter}'
            top_buffer = do_flush(False, top_buffer);
            dragon_arg1 = ''
            dragon_arg1 += '1200'
            saved_firstWord = self.firstWord
            call_Dragon('Wait', 'i', [dragon_arg1])
            self.firstWord = saved_firstWord
            top_buffer = do_flush(False, top_buffer);
            dragon_arg1 = ''
            dragon_arg1 += '{win+t}'
            saved_firstWord = self.firstWord
            call_Dragon('SendSystemKeys', 'si', [dragon_arg1])
            self.firstWord = saved_firstWord
            top_buffer = do_flush(False, top_buffer);
            dragon_arg1 = ''
            dragon_arg1 += '100'
            saved_firstWord = self.firstWord
            call_Dragon('Wait', 'i', [dragon_arg1])
            self.firstWord = saved_firstWord
            top_buffer += '{up}'
            top_buffer += '{enter}'
            top_buffer = do_flush(False, top_buffer);
            dragon_arg1 = ''
            dragon_arg1 += '5000'
            saved_firstWord = self.firstWord
            call_Dragon('Wait', 'i', [dragon_arg1])
            self.firstWord = saved_firstWord
            top_buffer += '26'
            top_buffer = do_flush(False, top_buffer);
            dragon_arg1 = ''
            dragon_arg1 += '1500'
            saved_firstWord = self.firstWord
            call_Dragon('Wait', 'i', [dragon_arg1])
            self.firstWord = saved_firstWord
            top_buffer += '{enter}'
            top_buffer = do_flush(False, top_buffer);
            dragon_arg1 = ''
            dragon_arg1 += '1000'
            saved_firstWord = self.firstWord
            call_Dragon('Wait', 'i', [dragon_arg1])
            self.firstWord = saved_firstWord
            top_buffer += '{alt+s}'
            top_buffer += '{down_2}'
            top_buffer += '{enter}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_29(words[1:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 46, '\'restart Jenkins sessions\'', e)
            self.firstWord = -1

    # 'resume previous session'
    def gotResults_30(self, words, fullResults):
        if self.firstWord<0:
            return
        try:
            top_buffer = ''
            top_buffer = do_flush(False, top_buffer);
            dragon_arg1 = ''
            dragon_arg1 += '100'
            saved_firstWord = self.firstWord
            call_Dragon('Wait', 'i', [dragon_arg1])
            self.firstWord = saved_firstWord
            top_buffer += '{alt+s}'
            top_buffer += '{down_2}'
            top_buffer += '{enter}'
            top_buffer = do_flush(False, top_buffer);
            self.firstWord += 1
            if len(words) > 1: self.gotResults_30(words[1:], fullResults)
        except Exception, e:
            handle_error('firefox.vcl', 48, '\'resume previous session\'', e)
            self.firstWord = -1

thisGrammar = ThisGrammar()
thisGrammar.initialize()

def unload():
    global thisGrammar
    if thisGrammar: thisGrammar.unload()
    thisGrammar = None
