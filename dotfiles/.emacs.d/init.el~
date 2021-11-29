

;;;emacs.d/init.el

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;
;; 
;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;
;; 目次
;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;





;;;;;;;;==============================================================
;;;;;;;;;;;;
;;;;;;;;;;;;パスの設定(極力init.el中で初めの方に書いた方が良い)
;;;;;;;;;;;;
;;;;;;;;==============================================================


;;;; サブディレクトリも自動でロードパスを追加する関数（add-to-load-path関数の定義）
  (defun add-to-load-path (&rest paths)
  (let (path)
  (dolist (path paths paths)
    (let ((default-directory (expand-file-name (concat user-emacs-directory path))))
    (add-to-list 'load-path default-directory)
    (if (fboundp 'normal-top-level-add-subdirs-to-load-path)
  (normal-top-level-add-subdirs-to-load-path))))))
;;
;;~/.emacs.d/elisp ディレクトリをロードパスに追加
;;(add-to-list 'load-path "~/projects/dotfiles/.emacs.d")
(add-to-list 'load-path "~/.emacs.d/elpa")
(add-to-list 'load-path "~/.emacs.d/elisp")
(add-to-list 'load-path "~/.emacs.d/elpa/doom-modeline-2.9.2/")
;;
;; 
;; ターミナル　パスを通していないので，以下を参照すること
;;  
;; 1，mktexlsr
;;  
;; sudo /usr/local/texlive/2014/bin/x86_64-darwin/mktexlsr
;;  
;; sudo /usr/local/texlive/2014/bin/x86_64-darwin/mktexlsr
     
;; 2,
;; /opt/local/bin/tools/latex tools.ins
;;  
;;  
;; 3,
;; /usr/local/texlive/texmf-local/tex/latex/local/misc/
;; /usr/local/texlive/texmf-local/tex/latex/local/misc/
;; にmacrosとpictureが入っている
;;  
;;  
;; 4，perlとの連携
;; /opt/local/lib/perl5/site_perl/5.16.3/darwin-thread-multi-2level
;;     /opt/local/lib/perl5/site_perl/5.16.3
;;     /opt/local/lib/perl5/vendor_perl/5.16.3/darwin-thread-multi-2level
;;     /opt/local/lib/perl5/vendor_perl/5.16.3
;;     /opt/local/lib/perl5/5.16.3/darwin-thread-multi-2level
;;     /opt/local/lib/perl5/5.16.3
;;     /opt/local/lib/perl5/site_perl
;;     /opt/local/lib/perl5/vendor_perl
;;
;;packageのディレクトリと，そのサブディレクトリをload-pathに追加
(add-to-load-path "elisp" "conf" "public_repos" "elpa" "site-lisp")
;;
;;
;;YaTeX関連のパス
;;2019/6/27 使うyatexを下の~/Library/emacs/yatexのものから変更した．
;;というのも，site-lisp以下にあるyatexpkg.elを編集したから．
;;今後もこのようなことが想定されるので，yatexはこちらに統一しよう．
;;(add-to-list 'load-path "~/library/emacs/yatex") ;;古いyatexの場所
;; 2020/10/06 他のmacとの協調性を考えて，homeを~で統一する．
(add-to-list 'load-path "~/.emacs.d/site-lisp/yatex1.81/")
(add-to-list 'load-path "~/.emacs.d/elpa/yatex-20200208.931")

(add-to-list 'load-path "~/.emacs.d/site-lisp/emacs-shell-mode-iterm-extensions/")

(add-to-list 'load-path "/Library/TeX/texbin")

;; icons in terminal
;; 2021/11/24 一旦disabled
;; https://github.com/sebastiencs/icons-in-terminal
;; (add-to-list 'load-path "~/.local/share/icons-in-terminal/")


;;Tex関係のパス
;;2019/7/9  使うtexliveを2018へ．いらないと思われるpathをコメントアウトした．
;;結果として，texlive/2018/texmf-distさえpathが通っていれば良さそうであることが判明した．
;;これは昔試したときにはダメだったので，なんらかの変更があったのだろうか？
(add-to-list 'load-path "/usr/local/texlive/2019/texmf-dist/")
;;
;;
;;https://emacs-jp.github.io/tips/environment-variable
(setq exec-path (parse-colon-path (getenv "PATH")))
;;
;;
;; aspell
;; https://texwiki.texjp.org/?Aspell
(add-to-list 'load-path "/opt/local/bin/")
;;
;;
;;
;;
;;


;;;;=================================
;;パッケージ管理
;;;;=================================

;;packageというemacs独自のパッケージ管理システムがあり，それを利用可能にするための記述である．
;;実際にパッケージを追加する方法は
;;M_x package-install
;;

;;https://www.wagavulin.jp/entry/2016/07/04/211631
;; 2021/2/23 emacs27ではいらないっぽいwarningが出る．
;;(package-initialize)

;;移植用．
;;installしたものをここのリストに追加しておく（将来的にはこの作業も自動化したい）
;;すると初回起動時に勝手にpackageからinstallしてくれる．
;;これは，usepackageをつかうことで自動化できるので，use-packageのみ初回に持ってくればよい
(defvar my-favorite-package-list
  '(
    use-package
    helm
    web-mode
    projectile
    auto-complete
    elscreen
    yasnippet
    howm
    neotree
    dumb-jump
    all-the-icons
    flycheck
    color-moccur
    undohist
    undo-tree
    quickrun
    monokai-theme
    atom-one-dark-theme
    doom-themes
    doom-modeline
    ;;Rainbow-Delimiters  ;;2020/4/14 なぜかerrorが出るようになった．packageで何かあったかも．
    )
  "packages to be installed")

(require 'package)
(add-to-list 'package-archives '("melpa" . "http://melpa.org/packages/"))
(add-to-list 'package-archives '("melpa-stable" . "http://stable.melpa.org/packages/") t)
(package-initialize)
(unless package-archive-contents (package-refresh-contents))
(dolist (pkg my-favorite-package-list)
  (unless (package-installed-p pkg)
    (package-install pkg)))




;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;
;; general setting 1
;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;;元々のemacsに備わっている機能をどうカスタマイズするかの設定
;;packageの類が全くいらない設定．

;;2020/1/11 一応残しておくが，start up messageがあっても別に困らない
;; no start up message
;(setq inhibit-startup-screen t)

;;(set-face-attribute 'default nil :font "DejaVu Sans Mono-14")
;;(set-face-attribute 'mode-line nil :font "DejaVu Sans Mono-30")

;;;; language setting
;;2020/4/1 （どうもこの設定がなくても上手く行っている感じはあるのだが，念のため設定する）
;;http://yohshiy.blog.fc2.com/blog-entry-273.html
(set-language-environment "Japanese")
(set-default-coding-systems 'utf-8)
(set-keyboard-coding-system 'utf-8)
(set-terminal-coding-system 'utf-8)
(set-buffer-file-coding-system 'utf-8)
(set-terminal-coding-system 'utf-8)
(prefer-coding-system 'utf-8)


;;emacs23.2以降では非推奨
;;(setq default-buffer-file-coding-system 'utf-8)


;;; ツールバーを非表示
(tool-bar-mode -1)
;;; メニューバーを非表示
(menu-bar-mode -1)
;;; スクロールバーを非表示
;; 2021/2/23 bigsurにしてからerrorが出るように．
;;(scroll-bar-mode -1)
;;;\C-kで改行を含めて削除
;;https://gist.github.com/yancya/4475969
(setq kill-whole-line t)
;;エラー音をならなくする．(doom-themeでエラー音の代わりにmode-lineを光らせるようにしてあるので，設定しなくてもok)
;;(setq ring-bell-function 'ignore)
;;bufferの終端を明示
;;https://github.com/emacs-jp/emacs-jp.github.com/issues/38
(setq-default indicate-empty-lines t)


;;;;auto-insert(テンプレートの挿入）
;;http://www.math.s.chiba-u.ac.jp/~matsu/emacs/emacs21/autoinsert.html
;;http://higepon.hatenablog.com/entry/20080731/1217491155

;;auto-insertの有効化
(require 'autoinsert)
(add-hook 'find-file-hooks 'auto-insert)
;;insertするサンプルファイルの置き場所
(setq auto-insert-directory "~/.emacs.d/elisp/insert/")
;;各ファイルによってテンプレートを切り替える
(setq auto-insert-alist
      (append '(
               ("\\.cpp$" . "template.cpp" )
               ("\\.h$"   . "template.h" )
               ("\\.cc$"  . "template.cc" )
              ) auto-insert-alist ))

;;;;; input special and control characters by "Option"
(setq ns-option-modifier 'none)


;;;;; cursor mode
(setq blink-cursor-interval 0.5)
(setq blink-cursor-delay 5.0)
(blink-cursor-mode 1)


;;recentf
;;https://www.emacswiki.org/emacs/RecentFiles
;;https://qiita.com/tadsan/items/68b53c2b0e8bb87a78d7
;;https://www.yokoweb.net/2017/01/18/emacs-recentf/
(defmacro with-suppressed-message (&rest body)
 ;; "Suppress new messages temporarily in the echo area and the `*Messages*' buffer while BODY is evaluated."
  (declare (indent 0))
  (let ((message-log-max nil))
    `(with-temp-message (or (current-message) "") ,@body)))
(setq recentf-save-file "~/.emacs.d/.recentf")
(setq recentf-max-saved-items 2000) ;;2000ファイルまで履歴保存する
(setq recentf-auto-cleanup 'never)  ;;存在しないファイルは消さない
(setq recentf-exclude '("/recentf" "COMMIT_EDITMSG" "/.?TAGS" "^/sudo:" "/\\.emacs\\.d/games/*-scores" "/\\.emacs\\.d/\\.cask/"))


(setq recentf-auto-save-timer (run-with-idle-timer 30 t 'recentf-save-list))
;;30秒ごとに .recentf を保存
(run-with-idle-timer 30 t '(lambda ()
     (with-suppressed-message (recentf-save-list))))
(recentf-mode 1)

;;キーバインド
(global-set-key (kbd "C-c r") 'recentf-open-files)
(bind-key "C-c っ" 'helm-recentf)
(bind-key "C-c t" 'helm-recentf)



;;;;;現在行のハイライト
;;2019/12/26 http://keisanbutsuriya.hateblo.jp/entry/2015/02/01/162035
;;このhl-line-modeについては，重くなるという指摘がある．
;;問題が顕在化してくるようなら他のmodeを使って代用することもできるようだ．
;;http://emacs.rubikitch.com/global-hl-line-mode-timer/
(global-hl-line-mode t)
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(doom-modeline-bar ((t (:background "#6272a4"))))
 '(flycheck-error ((t (:foreground "brightmazenta" :underline (:color "Foreground Color" :style line)))))
 '(flycheck-warning ((t (:foreground "green" :underline (:color "Foreground Color" :style line)))))
 '(font-lock-variable-name-face ((t (:foreground "orange2"))))
 '(hl-line ((t (:background "darkslategray"))))
 '(org-pomodoro-mode-line ((t (:foreground "#ff5555"))))
 '(org-pomodoro-mode-line-break ((t (:foreground "#50fa7b"))))
 '(vhl/default-face ((nil (:foreground "#FF3333" :background "#FFCDCD")))))

;; ;;色の一覧についてはここを参照
;; ;;https://nautilus-code.jp/articles/emacs_color_code/
;; ;;簡単な色はM-x list-colors-displayで表示可能（ここがうまく表示されない問題は，bashrcでTERMがおかしかったことに起因．そっちを参照すること）
;; (set-face-background 'hl-line "snow")
;; ;;文字色を上書きしないように！これ大事
;; ;;http://yuelab82.hatenablog.com/entry/terminal_now
;;(set-face-attribute 'hl-line nil :inherit nil)

;;これは他の書式の選択肢
;(custom-set-faces
;'(hl-line ((t (:background "gray64"))))
;)


;;;;;対応する括弧のハイライト．
;;2019/12/26 http://keisanbutsuriya.hateblo.jp/entry/2015/02/01/162035
(show-paren-mode t)
;;ハイライトのスタイル，これは対応する括弧のみハイライト
(setq show-paren-style 'parenthesis)
;;他に，expression（括弧で囲まれたところのハイライト）などがある



;;行数表示
;;(global-linum-mode t)
;;(set-face-foreground 'linum "gray64")
;;(setq linum-format "%5d  ")


;;括弧の自動挿入
;;2019/12/26 http://bhby39.blogspot.com/2014/02/emacs.html
;;2019/12/26 他の所と干渉しないかしばらくテストする必要あり．
(electric-pair-mode 1)


;; 選択領域を削除キーで一括削除
(delete-selection-mode t)

;; 空白を一度に削除
 (if (fboundp 'global-hungry-delete-mode)
     (global-hungry-delete-mode 1))

;;c系モードで，；を打った後に自動改行+インデント
;;2020/1/10
;;for文とかでも;を使うのだが，これらはyasnippetで自動挿入されるので使わないだろうという判断
(add-hook 'c-mode-common-hook
         '(lambda ()
            (c-toggle-auto-hungry-state 1) ;; センテンスの終了である ';' を入力したら、自動改行+インデント
           ; (define-key c-mode-base-map "\C-m" 'newline-and-indent) ;; RET キーで自動改行+インデント→これはすでにonになってる気がする
))



(use-package doom-themes
     :ensure t
     :custom
     (doom-themes-enable-italic t) ; if nil, italics is universally disabled
     (doom-themes-enable-bold t) ; if nil, bold is universally disabled
     :custom-face
     (doom-modeline-bar ((t (:background "#6272a4"))))
     :config
     ;; Load the theme (doom-one, doom-molokai, etc); keep in mind that each theme may have their own settings.
     (load-theme 'doom-dracula t)
     ;; ;; Enable flashing mode-line on errors(color:violet)
     (doom-themes-visual-bell-config)
     ;; Enable custom neotree theme (all-the-icons must be installed!)
     (doom-themes-neotree-config)
     ;; Corrects (and improves) org-mode's native fontification.
     (doom-themes-org-config))
;; (setq doom-themes-treemacs-theme "doom-colors") ; use the colorful treemacs theme
;; (doom-themes-treemacs-config)





;; ;;solarizedを設定する場合，現在melpa経由でダウンロードしたもの（./elpa/solarized...）と，別の作者によるもの（./themes/solarized..）がある．
;; ;;コメントアウトの色などに違いが見られる．

;; (add-to-list 'load-path "~/.emacs.d/elpa/solarized-theme-20200113.37")


;; ;;(add-to-list 'custom-theme-load-path "~/.emacs.d/themes/color-theme-solarized.el")
;; ;;(add-to-list 'custom-theme-load-path "~/.emacs.d/themes")
;; ;;(load-file "~/.emacs.d/themes/color-theme-solarized.el")


;; (add-to-list 'custom-theme-load-path "~/.emacs.d/elpa/solarized-theme-20200113.37")




;; (add-to-list 'load-path "~/.emacs.d/themes/emacs-color-theme-solarized-master")
;; (add-to-list 'custom-theme-load-path "~/.emacs.d/themes/emacs-color-theme-solarized-master")

;; ;;(require 'color-theme-solarized )
;; ;;(color-theme-solarized)

;; ;;(enable-theme 'solarized)

;; ;; (add-hook 'after-make-frame-functions
;; ;;           (lambda (frame)
;; ;;             (let ((mode (if (display-graphic-p frame) 'light 'dark)))
;; ;;               (set-frame-parameter frame 'background-mode mode)
;; ;;               (set-terminal-parameter frame 'background-mode mode))
;; ;;             (enable-theme 'solarized)))



;; ;;(frame-parameter nil 'background-mode)
;; (set-frame-parameter nil 'background-mode 'dark)
;; (set-terminal-parameter nil 'background-mode 'dark)
;; ;;(setq solarized-termcolors 16)
;; ;;(load-theme 'solarized t)
;; (load-theme 'solarized-dark t)





;;;;=================================
;; 拡張子によるmodeの指定．
;;;;=================================

;; https://blog.goo.ne.jp/dak-ikd/e/01b45dc521b48536fbd0ac4d6a4a4d6e
(add-to-list 'auto-mode-alist '("\\.pyx\\'" . python-mode))



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; all-the-icons
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;all-the-iconsはGUIでのみ有効である．
(use-package all-the-icons)
(setq all-the-icons-color-icons t)
(setq all-the-icons-icon-for-buffer t)
(setq all-the-icons-icon-for-dir t)
(setq all-the-icons-icon-for-file t)
(setq all-the-icons-icon-for-mode t)
(setq all-the-icons-icon-for-url t)
(setq all-the-icons-icon-for-weather t)
(setq all-the-icons-scale-factor 0.9)
(all-the-icons-octicon "file-binary")


;; icons-in-terminal
;;(require 'icons-in-terminal)
;; (icons-in-terminal-insert)
;; (icons-in-terminal-insert-faicon)
;; (icons-in-terminal-faicon "book")
;;(icons-in-terminal-icon-for-buffer)
;;(icons-in-terminal-icon-for-mode 'emacs-lisp-mode)
;;(icons-in-terminal-icon-for-file "template.el")

;;(use-package 'sidebar)
;;(global-set-key (kbd "C-x C-f") 'sidebar-open)
;;(global-set-key (kbd "C-x C-a") 'sidebar-buffers-open)

;;;;=================================
;;;; beacon（カーソルを光らせる）
;;;;=================================
;;
;;2020/4/8
;;https://qiita.com/Ladicle/items/feb5f9dce9adf89652cf
;;
(use-package beacon
    :custom
    (beacon-color "yellow")
    :config
    (beacon-mode 1))


;;;;=================================
;; dashboard（emacsの起動画面のカスタマイズ）
;;;;=================================
;;
;;2020/4/10
;;https://github.com/emacs-dashboard/emacs-dashboard
;;https://qiita.com/Ladicle/items/feb5f9dce9adf89652cf
;;https://qiita.com/hyakt/items/f4468facec0478e06f7a
;;
;;bookmarksはemacsの標準機能
;;http://tototoshi.hatenablog.com/entry/20101226/1293334388


(use-package dashboard
  :ensure t
  :custom
  (dashboard-set-navigator t)
  (dashboard-items '((recents . 15)
		     (projects . 5)
		     (bookmarks . 5)
		     (agenda . 10)))
  :config
  (dashboard-setup-startup-hook))

;;emacs daemonを使う時にもdashboardを起動する．（2020/5/8）
;;https://www.reddit.com/r/emacs/comments/8i2ip7/emacs_dashboard_emacsclient
(setq initial-buffer-choice (lambda () (get-buffer "*dashboard*")))
;;→なんか微妙な挙動を示しているので一時停止→2021/10/28 使用再開

;;ダッシュボードをもう一回開きたいとき．
;;https://qiita.com/minoruGH/items/d5f2975a76b6ca4ceb1c
(bind-key [f10] 'open-dashboard)
(bind-key [f10] 'dashboard-quit dashboard-mode-map)

(defun open-dashboard ()
  "Open the *dashboard* buffer and jump to the first widget."
  (interactive)
  (delete-other-windows)
  ;; Refresh dashboard buffer
  (if (get-buffer dashboard-buffer-name)
      (kill-buffer dashboard-buffer-name))
  (dashboard-insert-startupify-lists)
  (switch-to-buffer dashboard-buffer-name)
  ;; Jump to the first section
  (goto-char (point-min))
  (dashboard-goto-recent-files))

(defun quit-dashboard ()
  "Quit dashboard window."
  (interactive)
  (quit-window t)
  (when (and dashboard-recover-layout-p
             (bound-and-true-p winner-mode))
    (winner-undo)
    (setq dashboard-recover-layout-p nil)))

(defun dashboard-goto-recent-files ()
  "Go to recent files."
  (interactive)
  (funcall (local-key-binding "r")))





;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; dired（emacs標準ファイラ）
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; https://qiita.com/l3msh0/items/8665122e01f6f5ef502f
;; 起動は C-x d
;; + :: mkdir
;; d :: 削除マークをつける．
;; x :: 削除マークが付いたのを実際に削除．
;; R :: mv
;; C :: cp
;; D :: rm
;;(use-package icons-in-terminal-dired.el)
;;(set-fontset-font t '(#Xe000 . #Xf8ff) "icons-in-terminal")


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; symbol-overlay（単語ハイライト）
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;2020/4/7
;;https://qiita.com/blue0513/items/c0dc35a880170997c3f5
;;単語と言ってもspace区切りの物だけのようなので，yatexのようなdocumentで使うよりはcodingで使うものかも

;; use-packageを使う時のkey-bindについて．
;; https://www-he.scphys.kyoto-u.ac.jp/member/shotakaha/dokuwiki/doku.php?id=toolbox:emacs:keybind:start
;; https://github.com/jwiegley/use-package
(use-package symbol-overlay
  :ensure t

  :bind (("M-i" . symbol-overlay-put)
	 ("C-g" . symbol-overlay-remove-all) ;;ハイライトキャンセル
	 :map symbol-overlay-map
	 ("p" . symbol-overlay-jump-prev) ;; 前のシンボルへ
	 ("n" . symbol-overlay-jump-next));; 次のシンボルへ
  :config
  (add-hook 'prog-mode-hook #'symbol-overlay-mode)
  (add-hook 'markdown-mode-hook #'symbol-overlay-mode)
  (add-hook 'yatex-mode-hook #'symbol-overlay-mode)
  )





;;;;==============================
;; google this
;;;;==============================
;;;;==============================
;;2020/4/7
;;https://qiita.com/blue0513/items/c0dc35a880170997c3f5
;;https://qiita.com/takaxp/items/00245794d46c3a5fcaa8#設定
(use-package google-this
  :config
    (defun my:google-this ()
      "検索確認をスキップして直接検索実行"
      (interactive)
      (google-this (current-word) t)))


;;2020/10/06  ただのgだったけど，それだとけっこう被っちゃうので，gggにした．
(use-package selected)
(selected-global-mode 1)
(define-key selected-keymap (kbd "ggg") #'my:google-this)


;;;;==============================
;; imenu-list
;;;;==============================
;;;;==============================
(use-package imenu-list)




;;;;=================================
;;   modelineに関する一般的な設定
;;;;=================================
;;
;; 2020/3/2 現在の関数名をモードラインに表示
;; https://qiita.com/Klein/items/1f49eddcd94474f7a9ac
(which-function-mode t)

;;行番号，列番号の表示
(setq line-number-mode t)
(setq column-number-mode t)

;; save時にmode line を光らせる．（doom-modelineだと動くが，powerlineだと動かない．）
(add-hook 'after-save-hook
      (lambda ()
        (let ((orig-fg (face-background 'mode-line)))
          (set-face-background 'mode-line "dark green")
          (run-with-idle-timer 0.1 nil
                   (lambda (fg) (set-face-background 'mode-line fg))
                   orig-fg))))


;;https://qiita.com/blue0513/items/99476f4ae51f17600636
;;powerlineと同時に使うと表示してくれない．
(use-package total-lines)
(global-total-lines-mode t)
(defun my-set-line-numbers ()
  (setq-default mode-line-front-space
        (append mode-line-front-space
            '((:eval (format " (%d)" (- total-lines 1))))))) ;; 「" (%d)"」の部分はお好みで
(add-hook 'after-init-hook 'my-set-line-numbers)


;; (require 'flycheck-color-mode-line)
;; (eval-after-load "flycheck"
;;   '(add-hook 'flycheck-mode-hook 'flycheck-color-mode-line-mode))

;;マイナーモードの表示に関して
;;http://syohex.hatenablog.com/entry/20130131/1359646452



;;;;=================================
;;    doom-modeline
;;;;=================================
;;
;;
;;https://github.com/domtronn/spaceline-all-the-icons.el
;;http://8gu15.hatenablog.jp/entry/2018/12/06/071125
(use-package spaceline-all-the-icons
  :after spaceline
  :config (spaceline-all-the-icons-theme))

;;https://qiita.com/twitte_raru/items/6f02b6a8b6020a0e4f64
;;これは，どうもdoom-modeline-iconsと言うiconフォントを使っていて，それが文字化けの原因になっているようだ．
(require 'doom-modeline)
(doom-modeline-mode 1)
;;:custom
(setq doom-modeline-buffer-file-name-style 'truncate-with-project)
(setq doom-modeline-icon nil)

(setq doom-modeline-major-mode-icon nil)
;;Whether display the minor modes in the mode-line.
(setq doom-modeline-minor-modes nil)
;;(setq doom-modeline-icon (display-graphic-p))
(setq doom-modeline-buffer-state-icon nil)

;; Whether display the `lsp' state. Non-nil to display in the mode-line.
(setq doom-modeline-lsp t)


;; (defun setup-initial-doom-modeline ()
;;   (doom-modeline-set-modeline 'main t))
;; (add-hook 'doom-modeline-mode-hook #'setup-initial-doom-modeline)




;;modelineの表示がいらないmodeではmodelineを表示しない
;;2020/4/7 https://qiita.com/Ladicle/items/feb5f9dce9adf89652cf
(use-package hide-mode-line
    :hook
    ((neotree-mode imenu-list-minor-mode minimap-mode) . hide-mode-line-mode))

;;(require 'hide-mode-line)
;;(neotree-mode imenu-list-minor-mode minimap-mode) . hide-mode-line-mode)






;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;powerline-modeline
;;;;==============================
;;;;==============================
;;2020/4/7 今まで表示がよくなかったのだが，powerline.el本体を直接弄ることでseparatorに関する問題を解消

;; (require 'powerline)
;; (powerline-default-theme)

;; defaultでは見にくい色を変更
;; (set-face-attribute 'mode-line nil
;;                     :foreground "linen"
;;                     :background "skyblue"
;;                     :bold t
;;                     :box nil)

;;  (set-face-attribute 'powerline-active1 nil
;;                      :foreground "gray23"
;;                      :background "dodgerblue"
;;                      :bold t
;;                      :box nil
;;                      :inherit 'mode-line)

;;  (set-face-attribute 'powerline-active2 nil
;;                      :foreground "gray28"
;;                      :background "cornflowerblue"
;;                      :bold t
;;                      :box nil
;;                      :inherit 'mode-line)






;; (require 'spaceline-config)
;; (spaceline-spacemacs-theme)

;; (use-package spaceline-config
;;   :init
;;   (progn
;;     (setq powerline-default-separator 'slant)
;;     ;; anti aging power-line.
;;     (setq ns-use-srgb-colorspace nil))
;;   :config
;;   (progn
;;     (spaceline-emacs-theme)))

;; ;; paradox mode on
;; (spaceline-toggle-paradox-menu-on)

;; ;; anti aging power-line.
;; ;; (setq ns-use-srgb-colorspace t)
;; (mode-icons-mode)
;; (setq mode-icons-grayscale-transform nil)

;; (use-package spaceline-config)
;; (setq powerline-height 16)

;; (spaceline-emacs-theme)`




;; ;;;;;powerlineを元にした自作のmodeline
;; (defun shorten-directory (dir max-length)
;;   "Show up to `max-length' characters of a directory name `dir'."
;;   (let ((path (reverse (split-string (abbreviate-file-name dir) "/")))
;;         (output ""))
;;     (when (and path (equal "" (car path)))
;;       (setq path (cdr path)))
;;     (while (and path (< (length output) (- max-length 4)))
;;       (setq output (concat (car path) "/" output))
;;       (setq path (cdr path)))
;;     (when path
;;       (setq output (concat ".../" output)))
;;     output))

;; (defun powerline-my-theme ()
;;   "Setup the my mode-line."
;;   (interactive)
;;   (setq-default mode-line-format
;;                 '("%e"
;;                   (:eval
;;                    (let* ((active (powerline-selected-window-active))
;;                           (mode-line (if active 'mode-line 'mode-line-inactive))
;;                           (face1 (if active 'powerline-active1 'powerline-inactive1))
;;                           (face2 (if active 'powerline-active2 'powerline-inactive2))
;;                           (separator-left (intern (format "powerline-%s-%s"
;;                                                           powerline-default-separator
;;                                                           (car powerline-default-separator-dir))))
;;                           (separator-right (intern (format "powerline-%s-%s"
;;                                                            powerline-default-separator
;;                                                            (cdr powerline-default-separator-dir))))
;;                           (lhs (list (powerline-raw "%*" nil 'l)
;;                                      (powerline-buffer-size nil 'l)
;;                                      (powerline-raw mode-line-mule-info nil 'l)
;;                                      ;;; !!! ここから書き換えた !!!
;;                                      (powerline-raw
;;                                       (shorten-directory default-directory 15)
;;                                       nil 'l)
;;                                      (powerline-buffer-id nil 'r)
;;                                      ;;; !!! ここまで書き換えた !!!
;;                                      (when (and (boundp 'which-func-mode) which-func-mode)
;;                                        (powerline-raw which-func-format nil 'l))
;;                                      (powerline-raw " ")
;;                                      (funcall separator-left mode-line face1)
;;                                      (when (boundp 'erc-modified-channels-object)
;;                                        (powerline-raw erc-modified-channels-object face1 'l))
;;                                      (powerline-major-mode face1 'l)
;;                                      (powerline-process face1)
;;                                      (powerline-minor-modes face1 'l)
;;                                      (powerline-narrow face1 'l)
;;                                      (powerline-raw " " face1)
;;                                      (funcall separator-left face1 face2)
;;                                      (powerline-vc face2 'r)))
;;                           (rhs (list (powerline-raw global-mode-string face2 'r)
;;                                      (funcall separator-right face2 face1)
;;                                      (powerline-raw "%4l" face1 'l)
;;                                      (powerline-raw ":" face1 'l)
;;                                      (powerline-raw "%3c" face1 'r)
;;                                      (funcall separator-right face1 mode-line)
;;                                      (powerline-raw " ")
;;                                      (powerline-raw "%6p" nil 'r)
;;                                      (powerline-hud face2 face1))))
;;                      (concat (powerline-render lhs)
;;                              (powerline-fill face2 (powerline-width rhs))
;;                              (powerline-render rhs)))))))


;; (powerline-my-theme)



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;hiwin(非active windowの背景色)
;;;;==============================
;;;;==============================

;; 2021/11/19 どうもこいつを使うとemacsclientとの相性が悪い．

;; ;; 非アクティブウィンドウの背景色を設定
;; ;;2020/1/13
;; ;;http://emacs.rubikitch.com/hiwin/
;; (use-package hiwin
;;   :ensure t
;;   :config
;;   (hiwin-activate)
;;   ;;色を変更する場合
;;   ;;(set-face-background 'hiwin-face "gray80")
;; )


;;;;=====================================
;;    rainbow-delimiters（括弧の深さで色分け）
;;;;=====================================
;;
;;2020/4/6
;; https://yuelab82.hatenablog.com/entry/terminal_now
(use-package rainbow-delimiters
  :ensure t
  :config 
  (add-hook 'yatex-mode-hook 'rainbow-delimiters-mode)
   )


;;;;=====================================
;;    anzu（search中に合計の数などを表示する）
;;;;=====================================
;;
;;2020/4/7 doom-modelineでも使えるようになっている．
;;https://emacs-jp.github.io/packages/mode-line/anzu
(use-package anzu
  :config
  (global-anzu-mode t))


;;;;=====================================
;; open-junk-file（使い捨てファイルの作成）
;;;;=====================================
;;2020/4/10
;;https://qiita.com/ytanto/items/c6e624fa099d8d12a4db#open-junk-file
;;任意の書式のファイルをショトカ\C-x jで開けるので便利．

(when (require 'open-junk-file)
  (setq open-junk-file-format "${HOME}/Documents/emacs_junk/%Y-%m-%d-%H%M%S.")
  (global-set-key (kbd "C-x j") 'open-junk-file))


;;;;=====================================
;; mew
;;;;=====================================
;;
;; https://qiita.com/kai2nenobu/items/5dfae3767514584f5220
;; :config キーワードはライブラリをロードした後の設定などを記述．
;; よって，setqはconfigの中にかく．

;; 2021/10/28 mewを動かすためにいくつかsoftが必要だった．
;; stunnel (port install stunnel)
;; gpg (port install gnupg2)

;; master password::0.511MeV
;; pinentry password::0.511MeV

(use-package mew
  :config
  ;; IMAP(受信)用
  (setq mew-proto "%")
  (setq mew-user "tragic44cg@gmail.com")
  (setq mew-mail-domain "gmail.com")
  (setq mew-imap-server "imap.gmail.com")
  (setq mew-imap-user "tragic44cg@gmail.com")
  (setq mew-imap-auth  t)
  (setq mew-imap-ssl t)
  (setq mew-imap-ssl-port "993") ;; gmail
  ;;smtp(送信)用
  (setq mew-smtp-auth t)
  (setq mew-smtp-ssl t)
  (setq mew-smtp-ssl-port "465") ;; gmail
  (setq mew-smtp-user "tragic44cg@gmail.com")
  (setq mew-smtp-server "smtp.gmail.com")
  (setq mew-ssl-verify-level 0)
  (setq mew-use-cached-passwd t)

  ;;master passwd
  (setq mew-use-master-passwd t)

  ;;notification on modeline
  (setq mew-use-biff t)
  (setq mew-use-biff-bell t)
  (setq mew-biff-interval 1))


;;;;=====================================
;;elscreen（ウィンドウの分割）
;;;;=====================================
;;
;;2020/1/30 elscreenパッケージをELFAからダウンロード（emacs本に記述あり）
;;elscreenのprefix-keyはデフォルトで\C-zである．
;;変更したければ以下
;(setq elscreen-prefix-key (kbd "\C-t"))

;;\C-z c   ::create new screen
;;\C-z n   ::go to next screen
;;\C-z p   ::back to previous screen

;; elscreen（上部タブ）を導入する．
(require 'elscreen)
(elscreen-start)
;;;set-keyの変更．以下から持ってきた
;;https://qiita.com/blue0513/items/ff8b5822701aeb2e9aae
;; (global-set-key (kbd "s-t") 'elscreen-create)
;; (global-set-key "\C-l" 'elscreen-next)
;; (global-set-key "\C-r" 'elscreen-previous)
;; (global-set-key (kbd "s-d") 'elscreen-kill)

;;;タブの色表示．デフォルトのはother-screen-faceが見にくい．
;; (set-face-attribute 'elscreen-tab-background-face nil
;;                     :background "grey10"
;;                     :foreground "grey90")
;; (set-face-attribute 'elscreen-tab-control-face nil
;;                     :background "grey20"
;;                     :foreground "grey90")
;; (set-face-attribute 'elscreen-tab-current-screen-face nil
;;                     :background "grey20"
;;                     :foreground "grey90")
;; (set-face-attribute 'elscreen-tab-other-screen-face nil
;;                     :background "grey30"
;;                     :foreground "grey60")


;;以下は見やすさのためにやっておいたほうが良い．
;;; [X]を表示しない
(setq elscreen-tab-display-kill-screen nil)
;;; [<->]を表示しない
(setq elscreen-tab-display-control nil)


;; ;;; タブに表示させる内容を決定
;; (setq elscreen-buffer-to-nickname-alist
;;       '(("^dired-mode$" .
;;          (lambda ()
;;            (format "Dired(%s)" dired-directory)))
;;         ("^Info-mode$" .
;;          (lambda ()
;;            (format "Info(%s)" (file-name-nondirectory Info-current-file))))
;;         ("^mew-draft-mode$" .
;;          (lambda ()
;;            (format "Mew(%s)" (buffer-name (current-buffer)))))
;;         ("^mew-" . "Mew")
;;         ("^irchat-" . "IRChat")
;;         ("^liece-" . "Liece")
;;         ("^lookup-" . "Lookup")))
;; (setq elscreen-mode-to-nickname-alist
;;       '(("[Ss]hell" . "shell")
;;         ("compilation" . "compile")
;;         ("-telnet" . "telnet")
;;         ("dict" . "OnlineDict")
;;         ("*WL:Message*" . "Wanderlust")))



;;http://emacs.rubikitch.com/nyan-mode/
;;(nyan-mode 1)


;;;;=================================
;;   neotree（サイドバー）
;;;;=================================
;;
;;
;; 2020/1/13 他にdiredというのもあって，こっちの方が機能豊富らしい．
;; https://qiita.com/minoruGH/items/2034cad4efe8c5dee4d4
(use-package neotree
  :bind ("\C-q" . neotree-toggle)   ;;neotreeの起動を\C-qへ変更
  :config
  ;; 隠しファイルをデフォルトで表示
  (setq neo-show-hidden-files t)
  ;; グラフィックはemacs-nwでは使用不可．
  (setq neo-theme (if (display-graphic-p) 'icons 'arrow))
  (setq neo-theme 'icons)
  ;;https://www.emacswiki.org/emacs/NeoTree
  (setq neo-smart-open t)
  ;; (display-graphic-p)
 )



;;;;=================================
;;    howm（メモ書き環境）
;;;;=================================
;;
;;2020/2/8 MELPAからインストール（emacs本に記述あり）
;;既存のメモ書きとの差別化を図る．

;;2020/5/8 org-modeとの統合について，一旦停止

;;howmメモ保存の場所
(setq howm-directory (concat user-emacs-directory "howm"))

;;howm-menuの言語::japanease
(setq howm-menu-lang 'ja)

;;howmメモを1年1ファイルにする．
;;%Yは年，%mは月，%dは日を表す．
(setq howm-file-name-format "%Y/%Y.howm")

;; ;;howmのヘッダを変更する．これはorgとの共存のため
;; ;; ← howm のロードより前に書くこと
;; ;;https://howm.osdn.jp/cgi-bin/hiki/hiki.cgi?DateFormat
;; (setq howm-view-title-header "*") 

;;howm-mode読み込み
(when (require 'howm nil t)
  ;;\C-c,,でhowm-menuを起動（これはデフォルトになってるっぽい）
  ;;(define-key global-map (kbd "\C_c ,,") 'howm-menu)
  )


;;以下，org-modeのtodoをhowmのメニューに表示するためのtips

;; ;;日付のフォーマット変更
;; (setq howm-dtime-format (concat "<" howm-dtime-body-format ">"))
;; (setq howm-insert-date-format "<%s>")



;; ;;日付検索のフォーマット変更
;; (setq howm-reminder-regexp-grep-format (concat "<" howm-date-regexp-grep "[ :0-9]*>%s"))
;; (setq howm-reminder-regexp-format (concat "\\(<" howm-date-regexp "[ :0-9]*>\\)\\(\\(%s\\)\\([0-9]*\\)\\)"))

;; ;;今日の日付を挿入するフォーマット変更
;; (setq howm-reminder-today-format (format howm-insert-date-format howm-date-format))

;; ;;ついでにhowmでdoneした時にorg-modeでもdoneされるようにする．
;; (defadvice howm-action-lock-done-done(after my-org-todo-done () activate) (org-todo))




;;;;=================================
;; which-key（key-bindを表示してくれる）
;;;;=================================
;;
;;2020/4/10
;;https://qiita.com/Ladicle/items/feb5f9dce9adf89652cf
  (use-package which-key
    :diminish which-key-mode
    :hook (after-init . which-key-mode))

;;;;=================================
;; amx（alternative interface for M-x）
;;;;=================================
;;
;;2020/4/10
;;M-xでコマンドを実行した時，Kbdがあればそれを表示する．
;;https://qiita.com/Ladicle/items/feb5f9dce9adf89652cf
(use-package amx)


;;;;=================================
;; clmemo with clgrep （Change-Log支援）
;;;;=================================
;;
;;2020/4/13
;;change-logを本格的に使えるようにメスを入れる．
;;http://bigfatcat.hateblo.jp/entry/20071010/1192025644
;;https://at-aka.blogspot.com/p/change-log.html
;;http://ta2o.net/doc/zb/0016.html
;;https://gan2-2.hatenadiary.org/entry/20071226/1198645571
;;C-c C-q でメモを開く前の状態に戻る。
;; C-c C-g でメモを検索(メモの画面で)。
;; C-c C-t C-c C-g でメモのタイトルを検索。
;; C-u C-x M でメモを開く。
;;C-c ( uでurltagを自動挿入．

;; 名前，メールアドレス，ChangeLog メモへのパス
(setq user-full-name "天野智仁")
(setq user-mail-address "amanotomohito@shoukaku.local")
(setq clmemo-file-name "~/works/codes/diary/diary.txt")
(setq clmemo-time-string-with-weekday t)
(autoload 'clmemo "clmemo" "ChangeLog memo mode." t)
;;key bind setting
;;global-set-keyとdefine-keyでは少し使い方が違うらしい
(global-set-key "\C-cd" 'clmemo)

;; 補完されるタイトルのリスト
(setq clmemo-title-list
      '("Ruby" "Book" "Idea" "safari" "emacs" "mac" "tex"))
(autoload 'clgrep "clgrep" "grep mode for ChangeLog file." t)
(autoload 'clgrep-title "clgrep" "grep first line of entry in ChangeLog." t)
(autoload 'clgrep-header "clgrep" "grep header line of ChangeLog." t)
(autoload 'clgrep-other-window "clgrep" "clgrep in other window." t)
(autoload 'clgrep-clmemo "clgrep" "clgrep directly ChangeLog MEMO." t)
(add-hook 'change-log-mode-hook
          '(lambda ()
             (define-key change-log-mode-map "\C-c\C-g" 'clgrep)
             (define-key change-log-mode-map "\C-c\C-t" 'clgrep-title)))



;;;;=================================
;; flycheck(構文チェック)
;;;;=================================
;;
;;2020/2/8 MELPAからinstall（emacs本に記述あり）
;;Cなどの構文チェックが可能
;;基本的には自動でスペルチェックをして，おかしいところを下線で教えてくれる．

;;全てのmodeでフライチェックを有効にする．
;;http://keisanbutsuriya.hateblo.jp/entry/2017/06/21/015353
;;(global-flycheck-mode)

;;yatexには標準で対応していないらしいので，それを追加する
;;http://mtino1594.hatenablog.com/entry/2019/04/07/200000#use-package-の大まかな使い方
;;https://qiita.com/noriaki/items/8122e83867ff0cdb5d13
;;http://mtino1594.hatenablog.com/entry/2019/04/07/200000#flycheck-による文法チェック
;;http://cha.la.coocan.jp/doc/EmacsFlycheck.html
(use-package flycheck
  :ensure t
  :hook (after-init . global-flycheck-mode)
  :config
  (flycheck-add-mode 'tex-chktex 'yatex-mode)
  (flycheck-add-mode 'tex-lacheck 'yatex-mode))



;;http://cha.la.coocan.jp/doc/EmacsFlycheck.html#org814f11c

;;;;=================================
;;   aspell
;;;;=================================
;;
;; (setq-default ispell-program-name "aspell")
;; (with-eval-after-load "ispell"
;;   (setq ispell-local-dictionary "en_US")
;;   (add-to-list 'ispell-skip-region-alist '("[^\000-\377]+")))


 ;; aspellのリンク
  (setq-default ispell-program-name "aspell")
 
  ;; 日英混文の処理
  (with-eval-after-load "ispell"
    (setq ispell-local-dictionary "en_US")
    (add-to-list 'ispell-skip-region-alist '("[^\000-\377]+")))
 
 
  ;; https://qiita.com/walking_with_models/items/da8eaf4afa39cf4ecd4a
  ;; fly-spell
  ;; configは，パッケージを読み込んだ後の設定．
  (use-package flyspell
    :ensure t
    :hook (yatex-mode . flyspell-mode)
    :config
    (set-face-attribute 'flyspell-duplicate nil
                       :foreground "white"
                       :background "orange" :box t :underline nil)
    (set-face-attribute 'flyspell-incorrect nil
                       :foreground "white"
                       :background "red" :box t :underline nil)
    )
 

;;;;=================================
;; git-gutter
;;;;=================================
;;
;;2020/4/7 git差分を表示してくれる．
;;こいつの問題点は，linum-modeとの併用に問題が生じてしまう点．（と言っても見た目が崩れるだけだが）
;;解決としてgit-gutter-fringeと言うのも開発されているが，それはemacs-nwなどのtty frameでは動作しない．
;;git-gutterとgit-gutter+があって，なぜかgit-gutter+のみ正常に動作した．
;;https://github.com/nonsequitur/git-gutter-plus
;;https://blog.bokuweb.me/entry/emcas-nyumon
(use-package  git-gutter+
  :ensure t
  :config
  (global-git-gutter+-mode t))

;;;;=================================
;; Auto Complete（予測補完）
;;;;=================================
;;
;; ;;2019/12/26
;; (require 'auto-complete-config)
;; (ac-config-default)
;; (add-to-list 'ac-modes 'text-mode)         ;; text-modeでも自動的に有効にする
;; (add-to-list 'ac-modes 'fundamental-mode)  ;; fundamental-mode
;; (add-to-list 'ac-modes 'org-mode)
;; ;;(add-to-list 'ac-modes 'yatex-mode) 
;; (ac-set-trigger-key "TAB")
;; (setq ac-use-menu-map t)       ;; 補完メニュー表示時に\C-n,\C-pで補完候補選択
;; (setq ac-use-fuzzy t)          ;; 曖昧マッチ

;;;;=================================
;;Company（予測補完）
;;;;=================================
;;
;;2020/4/10
;;auto completeよりcompany modeの方が一般的らしいので乗り換えた．
(use-package company
  :ensure t
  :hook (after-init . global-company-mode))

;;tex/latex用の補完はcompany-math
;;http://mtino1594.hatenablog.com/entry/2019/04/07/200000#use-package-の大まかな使い方
;;数学記号の補完は YaTeX のイメージ補完に一任する場合は company-math-symbols-latex の行を消す．
(use-package company-math
  :ensure t
  :demand t
  :after (company yatex)
  :config
  (push 'company-math-symbols-latex company-backends)
  (push 'company-latex-commands company-backends))



;;;;=================================
;; lsp-mode 
;;;;=================================

(use-package lsp-mode)
;; config
(setq lsp-print-io nil)
(setq lsp-trace nil)
(setq lsp-print-performance nil)
(setq lsp-auto-guess-root t)
(setq lsp-document-sync-method 'incremental)
(setq lsp-response-timeout 5)

;; hook
(add-hook 'yatex-mode-hook #'lsp)

;; func
(defun lsp-mode-init ()
    (lsp)
    (global-set-key (kbd "M-*") 'xref-pop-marker-stack)
    (global-set-key (kbd "M-.") 'xref-find-definitions)
    (global-set-key (kbd "M-/") 'xref-find-references))


;;;;=================================
;; lsp-ui
;;;;=================================

(use-package lsp-ui)

;; config
(setq lsp-ui-doc-enable t)
(setq lsp-ui-doc-header t)
(setq lsp-ui-doc-include-signature t)
(setq lsp-ui-doc-max-width 150)
(setq lsp-ui-doc-max-height 30)
(setq lsp-ui-peek-enable t)

;; hook
(add-hook 'lsp-mode-hook 'lsp-ui-mode)

;;;;=================================
;; magit
;;;;=================================

;; https://qiita.com/roses-ug/items/5205706df2655130f69e
;; https://qiita.com/maueki/items/70dbf62d8bd2ee348274
(use-package magit
  :bind
  ("M-g" . magit-status)
  )

;; リポジトリ作成：M-x magit-init
;; magitへの入り口：M-x magit-status
;; ? :: magit-statusで?キーを押すとコマンド一覧が出るので「迷ったらまず?」を覚えておくとよい。
;; s :: stagingをする．
;; c :: コミットモード，ここでコメントを売って，C-c C-cでコミット完了．



;;;;=================================
;; shell-modeでescape-sequenceを読み込む
;;;;=================================

;;2020/4/7
;;https://iriya-ufo.hateblo.jp/entry/20080411/1207890141
;;試してみたけど，これでもzshプロンプトは改善されなかった．
;;(autoload 'ansi-color-for-comint-mode-on "ansi-color"
 ;;         "Set `ansi-color-for-comint-mode' to t." t)
;;(add-hook 'shell-mode-hook 'ansi-color-for-comint-mode-on)




;;;;==============================;;;;
;;;;==============================;;;;
;; yasnippet 関連の設定
;;;;==============================;;;;
;;;;==============================;;;;


;;2019/12/31
;;書式の補完はこっち．テンプレートを自動で挿入してくれる．
;;http://vdeep.net/emacs-yasnippet
;yasnippetについてはこの記事では改めて説明しませんが、irony-modeと併用することで関数の引数部分まで補完ができるようになるので、入れておくと便利です。もちろん、yasnippet単体でも定形パターンの挿入に活躍します。C++11のイディオムはデフォルトでは用意されていないものが多いので、よく使うパターンは自分で登録しておくとよいでしょう。
;;https://qiita.com/alpha22jp/items/90f7f2ad4f8b1fa089f4
;;https://futurismo.biz/archives/3071
;;https://www.m3tech.blog/entry/emacs-web-service

;;公式のyasnippet-snippetsがあるから，これも入れること．
;;これに関して，latex-modeのフォルダをcpしてyatex-modeと言うフォルダも作っておくと，yatex-modeでもsnippetが動くので便利

;; ;; 自分用・追加用テンプレート -> mysnippetに作成したテンプレートが格納される
;; (require 'yasnippet)
;; (require 'yasnippet-snippets)
;; (setq yas-snippet-dirs
;;       '("~/.emacs.d/mysnippets"
;;         ;"~/.emacs.d/yasnippets"
;; 	;"~/.emacs.d/yasnippets/snippets"
;; 	"~/.emacs.d/elpa/yasnippet-snippets-20200403.1026/snippets"
;;         ))

;; ;; 既存スニペットを挿入する
;; (define-key yas-minor-mode-map (kbd "C-x i i") 'yas-insert-snippet)

;; ;; 新規スニペットを作成するバッファを用意する
;; (define-key yas-minor-mode-map (kbd "C-x i n") 'yas-new-snippet)

;; ;; 既存スニペットを閲覧・編集する
;; (define-key yas-minor-mode-map (kbd "C-x i v") 'yas-visit-snippet-file)

;; (yas-global-mode 1)



;; ;;;;==============================;;;;
;; ;;;;==============================;;;;
;; ;; color-moccur
;; ;;;;==============================;;;;
;; ;;;;==============================;;;;

;; ;;2020/2/24
;; ;;https://gist.github.com/d-kuro/352498c993c51831b25963be62074afa

;; (when (require 'color-moccur nil t)
;;   ;;M-oにoccur-by-moccurを割り当て
;;   (define-key global-map (kby "\M-o") 'occur-by-moccur)
;;   ;;スペース区切りでand検索
;;   (setq moccur-split-word t)
;;   ;;ディレクトリ検索の時に除外するファイル
;;   (add-to-list 'dmoccur-exclusion-mask "\\.DS_Store")
;;   (add-to-list 'dmoccur-exclusion-mask "^#.+#$"))



;;;;========================
;; undohist and undo-tree
;;;;========================
;;
;;2020/2/24
;; https://qiita.com/ytanto/items/c6e624fa099d8d12a4db

;;undohist
;;emacsのデフォルト機能undoを永続的に使えるようにする
;;undo自体は\C-x u で，一つ前の操作を取り消せる
(when (require 'undohist nil t)
  (undohist-initialize))

;;undo-tree
;;undoの履歴を辿ることができる．\C-uでundoを実行すると別bufferにtreeを出してくれる．
;;戻したい所にcursorを移動して，qでbufferを抜ける．
(when (require 'undo-tree nil t)
  ;; C-'にredoを割り当てる（通常のundoと差別化したい時に使う．defaultではundoと同じkbyで，undoを上書きする）
  ;; (define-kry global-map (kby "\C-'") 'undo-tree-redo)
  (global-undo-tree-mode))

;;;;==============================;;;;
;;;;==============================;;;;
;; point-undo
;;;;==============================;;;;
;;;;==============================;;;;

;;2020/2/24 elpaに存在せず
;;http://emacs.rubikitch.com/sd1509-safeguard-undo-redo/


;;;;=======================
;; volatile-highlights
;;;;=======================

;;2020/5/31 ペーストした時に視覚的にハイライト
;;https://qiita.com/Ladicle/items/feb5f9dce9adf89652cf

  (use-package volatile-highlights
    :diminish
    :hook
    (after-init . volatile-highlights-mode)
    :custom-face
    (vhl/default-face ((nil (:foreground "#FF3333" :background "#FFCDCD")))))

;;;;=======================
;; quick-run
;;;;=======================
;;
;;2020/2/24
;;https://qiita.com/lethe2211/items/2271fd3530248eb7db62
(use-package quickrun)

;;;;=======================
;; gtag.el
;;;;=======================

;; (use-package gtags
;;   :config
;;   ;;gtags-modeのkbyを有効にする
;;   (setq gtags-suggested-key-mapping t)
;;   ;;file保存時に自動でtagをupdate
;;   (setq gtags-mode-auto-update t)
;;   )



;;;;=======================
;; helm
;;;;=======================
;;2020/2/26
(use-package helm-config)

;;;;=======================
;; highlight-indentaiton
;;;;=======================

;;2020/3/2
;;indent-guideというのもある
;;どうもelpaにないので，自分で持ってくる必要あり
;;https://blog.iss.ms/2012/03/17/095152
;;https://github.com/antonj/Highlight-Indentation-for-Emacs
(use-package highlight-indentation
  :config
  ;;(highlight-indentation-mode t)
  (add-hook 'c-mode-hook 'highlight-indentation-mode)
  ;;(add-hook 'yatex-mode-hook 'highlight-indentation-mode)
  )

;;;;==============================;;;;
;;;;==============================;;;;

;; fill-column-indicator
;;;;==============================;;;;
;;;;==============================;;;;

;(setq fill-column 85)

;; (use-package fill-column-indicator
;;   :hook
;;   ((markdown-mode
;;     org-mode
;;    git-commit-mode) . fci-mode))

;;;;==============================;;;;
;;;;==============================;;;;
;; dumb-jump
;;;;==============================;;;;
;;;;==============================;;;;

;;2020/1/11
;;tagを使わずにジャンプしてくれるやつ
;;http://blog.livedoor.jp/tek_nishi/archives/9626252.html

;; C-M-g ジャンプ
;; C-M-p 戻る
;; C-M-q チラ見

(use-package dumb-jump
  :config
  ;;標準キーバインドを指定する．
  (setq dumb-jump-mode t)
  )

;;;;==============================
;; org-modeの設定
;;;;==============================
;;;;==============================
;;org-modeは標準で入っているので，org自体のインストールは不要

;;org-modeで初めから画像で表示（gnu emacsのみ）
;;(setq org-startup-with-inline-images t)
;;(setq org-display-inline-images t)

;;org-modeでの画像の大きさの指定．（大きすぎると，emacsがフリーズする）
;;このように配列で指定すると，最初はorgファイル内の設定を優先してくれる．
;;https://www.reddit.com/r/emacs/comments/55zk2d/adjust_the_size_of_pictures_to_be_shown_inside/
;;(setq org-image-actual-width '(100))


;;howm-modeでもorg-modeを起動
;;http://nobunaga.hatenablog.jp/entry/2015/10/25/161305
;(add-hook 'org-mode-hook 'howm-mode)

;;howm-modeでもorg-modeを起動
;(add-to-list 'auto-mode-alist '("\\.howm$" . org-mode))
;(add-to-list 'auto-mode-alist '("\\.txt$" . org-mode))

;;https://stakizawa.hatenablog.com/entry/20091025/t1
;;http://emacs.rubikitch.com/toggle-truncate-lines/
;;https://saphir-jaune.hatenablog.com/entry/2018/04/29/003516
;;https://emacs.stackexchange.com/questions/51989/how-to-truncate-lines-by-default
;(set-default 'truncate-lines nil)
;(setq truncate-partial-width-windows nil)

;; org-modeでの強調表示を可能にする
(add-hook 'org-mode-hook 'turn-on-font-lock)

;;org-modeはデフォルトで折り返し禁止．（これはagendaとかのためだと思われる）
;;https://oversleptabit.com/archives/5640
;;https://passingloop.tumblr.com/post/12886175913/org-mode-で行を折り返したくないときは
;;(setq org-startup-truncated nil)
;;そこで，ファイルの先頭に
;;# -*- truncate-lines: nil; -*- 
;;を入れておくと折り返しが有効になる．

;; LOGBOOK drawerに時間を格納する
(setq org-clock-into-drawer t)

;;org-directory（これがサーバのディレクトリになるらしい）
;;https://ponkotuy.hatenadiary.org/entry/20110204/1296846549
(setq org-directory "~/diary/")

;; org-directory内のファイルすべてからagendaを作成する
(setq my-org-agenda-dir '( ;"~/.emacs.d/howm/2020/"
			   "~/programs/" ))
;;ちょっとうえの設定がうまく行っていないようなので，とりあえず手でファイルを指定する．
;;これも失敗した． 何がいけないのかわからない．しかし，
;;https://orgmode.org/manual/Agenda-Files.html
;;を参考にして，\C [ で開いているファイルをorg-agenda-filesに追加できる．
(setq org-agenda-files '( "~/programs/test.org"
	                  "~/diary/added.org"
			  "~/diary/diary.org"
			  ;"~/.emacs.d/howm/2020/2020.howm"
			  ))

;;org-agendaのキーバインドの設定
(global-set-key (kbd "C-c a") 'org-agenda)

;; TODO状態のカスタマイズ
(setq org-todo-keywords
      '((sequence "TODO(t)" "WAIT(w)" "NOTE(n)"  "|" "DONE(d)" "SOMEDAY(s)" "CANCEL(c)")))

;; DONEの時刻を記録
(setq org-log-done 'time)

;;http://karasunoblog.blog20.fc2.com/blog-entry-43.html
;;http://karasunoblog.blog20.fc2.com/blog-entry-13.html
;;http://bocchies.hatenablog.com/entry/2016/09/12/185551

;; MobileOrgで新しく作ったノートを保存するファイルの名前を設定（pullしたデータの置き場）
(setq org-mobile-inbox-for-pull "~/diary/added.org")
;; Dropbox直下のMobileOrgフォルダへのパスを設定（mobile-orgファイルの場所）
(setq org-mobile-directory "~/Documents/clouds/Dropbox/Apps/MobileOrg")


;; Org-captureの設定
;;http://ganmacs.hatenablog.com/entry/2016/04/01/164245
;;http://www.mhatta.org/wp/2018/08/16/org-mode-101-1/#org-modeの本当に最低限の設定

;; Org-captureを呼び出すキーシーケンス
(global-set-key (kbd "\C-c c") 'org-capture)

;; Org-captureのテンプレート（メニュー）の設定
;; ここにアイコンを入れると見やすくてよい．
(setq org-capture-templates
      '(("n" " Note" entry (file+headline "~/diary/diary.org" "Notes")
         "* %?\nEntered on %U\n %i\n %a")
        ("t" "Note2" entry (file+headline "~/Documents/clouds/Dropbox/Apps/MobileOrg/mobileorg.org" "Notes2")
         "* %?\nEntered on %U\n %i\n %a")
        ))



;;;org-pomodoro
;;https://qiita.com/Ladicle/items/feb5f9dce9adf89652cf
(use-package org-pomodoro
    :after org-agenda
    :custom
    (org-pomodoro-ask-upon-killing t)
    (org-pomodoro-format "%s")
    (org-pomodoro-short-break-format "%s")
    (org-pomodoro-long-break-format  "%s")
    :custom-face
    (org-pomodoro-mode-line ((t (:foreground "#ff5555"))))
    (org-pomodoro-mode-line-break   ((t (:foreground "#50fa7b"))))
    :hook
    (org-pomodoro-started . (lambda () (notifications-notify
                                               :title "org-pomodoro"
                           :body "Let's focus for 25 minutes!"
                           :app-icon "~/.emacs.d/img/001-food-and-restaurant.png")))
    (org-pomodoro-finished . (lambda () (notifications-notify
                                               :title "org-pomodoro"
                           :body "Well done! Take a break."
                           :app-icon "~/.emacs.d/img/004-beer.png")))
    :config
    :bind (:map org-agenda-mode-map
                ("p" . org-pomodoro)))


;;org-bullets は*を変更できるやつ.
(use-package org-bullets
      :custom (org-bullets-bullet-list '("" "" "" "" "" "" "" "" "" ""))
      :hook (org-mode . org-bullets-mode))

;;org-agendaの表示を変える．
 (setq org-agenda-current-time-string "← now")
    (setq org-agenda-time-grid ;; Format is changed from 9.1
        '((daily today require-timed)
          (0900 01000 1100 1200 1300 1400 1500 1600 1700 1800 1900 2000 2100 2200 2300 2400)
          "-"
      "────────────────"))



;;;;==============================
;; py-autopep8 
;;;;==============================
;;;;==============================

; 20200713 pythonで，自動でコード規約に従ってくれる．
; https://ksknw.hatenablog.com/entry/2016/05/07/171239
(use-package py-autopep8)
; これは一行上限を200文字へ．
(setq py-autopep8-options '("--max-line-length=200"))
(setq flycheck-flake8-maximum-line-length 200)
(py-autopep8-enable-on-save)



;;;;=================================
;;    YaTeX 関連の設定
;;;;=================================

;;2019/5/26
;;emacs26で動作させるために必要なようだ
;; http://moyse.hatenablog.com/entry/2017/01/30/144508
;;実際，emacsでtexファイルを開くと
;;File mode specification error: (void-function string-to-int)
;;というエラーを吐く．
(defun string-to-int (string &optional base)
  (string-to-number string base))

;;http://mtino1594.hatenablog.com/entry/2019/04/07/200000#flycheck-による文法チェック
;; (defvar my-YaTeX-section-alist
;;   '(("part" . 0)
;;     ("chapter" . 1)
;;     ("section" . 2)
;;     ("subsection" . 3)
;;     ("subsubsection" . 4)
;;     ("paragraph" . 5)
;;     ("subparagraph" . 6)))

;; (defvar my-YaTeX-metasection-list
;;   '("documentclass"
;;     "begin{document}" "end{document}"
;;     "frontmatter" "mainmatter" "appendix" "backmatter"))

;; (defvar my-YaTeX-outline-regexp
;;   (concat (regexp-quote "\\")
;;       (regexp-opt (append my-YaTeX-metasection-list
;;                   (mapcar #'car my-YaTeX-section-alist))
;;               t)))

;; (defvar my-YaTeX-outline-promotion-headings
;;   '("\\chapter" "\\section" "\\subsection"
;;     "\\subsubsection" "\\paragraph" "\\subparagraph"))

;; (defun my-YaTeX-outline-level ()
;;   (if (looking-at my-YaTeX-outline-regexp)
;;       (1+ (or (cdr (assoc (match-string 1) my-YaTeX-section-alist)) -1))
;;     1000))

;; (defun my-YaTeX-with-outline ()
;;   (outline-minor-mode 1)
;;   (setq-local outline-regexp my-YaTeX-outline-regexp)
;;   (setq-local outline-level #'my-YaTeX-outline-level)
;;   (setq-local outline-promotion-headings my-YaTeX-outline-promotion-headings))


;; (add-hook 'yatex-mode-hook 'my-YaTeX-with-outline)

;; (use-package outline-magic
;;   :ensure t
;;   :preface
;;   (defun my-outline-move-subtree-down (&optional arg)
;;     "Move the currrent subtree down past ARG headlines of the same level.
;; If the current subtree is folded, call `outline-hide-subtree' after move down."
;;     (interactive "p")
;;     (let* ((headers (or arg 1))
;;            (movfunc (if (> headers 0) 'outline-get-next-sibling
;;                       'outline-get-last-sibling))
;;            (ins-point (make-marker))
;;            (cnt (abs headers))
;;            (folded (save-match-data
;;                      (outline-end-of-heading)
;;                      (outline-invisible-p)))
;;            beg end txt)
;;       ;; Select the tree
;;       (outline-back-to-heading)
;;       (setq beg (point))
;;       (outline-end-of-subtree)
;;       (if (= (char-after) ?\n) (forward-char 1))
;;       (setq end (point))
;;       ;; Find insertion point, with error handling
;;       (goto-char beg)
;;       (while (> cnt 0)
;;         (or (funcall movfunc)
;;             (progn (goto-char beg)
;;                    (error "Cannot move past superior level")))
;;         (setq cnt (1- cnt)))
;;       (if (> headers 0)
;;           ;; Moving forward - still need to move over subtree
;;           (progn (outline-end-of-subtree)
;;                  (if (= (char-after) ?\n) (forward-char 1))))
;;       (move-marker ins-point (point))
;;       (setq txt (buffer-substring beg end))
;;       (delete-region beg end)
;;       (insert txt)
;;       (goto-char ins-point)
;;       (if folded (outline-hide-subtree))
;;       (move-marker ins-point nil)))
;;   :bind (:map outline-minor-mode-map
;;           ("C-<tab>" . outline-cycle)
;;           ("M-<left>" . outline-promote)
;;           ("M-<right>" . outline-demote)
;;           ("M-<up>" . outline-move-subtree-up)
;;           ("M-<down>" . outline-move-subtree-down))
;;   :demand t
;;   :after (outline)
;;   :config
;;   (advice-add 'outline-move-subtree-down :override #'my-outline-move-subtree-down))



;;;;;;;;;;;;;;;;;;;;;
;;自動でyatexを起動
;;;;;;;;;;;;;;;;;;;;

(autoload 'yatex-mode "yatex" "Yet Another LaTeX mode" t)
(setq auto-mode-alist
      (append '(("\\.tex$" . yatex-mode)
		("\\.ltx$" . yatex-mode)
		("\\.cls$" . yatex-mode)
		("\\.sty$" . yatex-mode)
		("\\.clo$" . yatex-mode)
		("\\.bbl$" . yatex-mode)) auto-mode-alist))


(setq YaTeX-inhibit-prefix-letter t)
;;漢字コードの設定
;;https://texwiki.texjp.org/?YaTeX#q88c5ad1
;;nilにしておいていちいちtexファイルで指定するか，4（UTF-8）かを選ぶのが良さそう
(setq YaTeX-kanji-code 4)
;;type-set時のmessageの文字コード
(setq YaTeX-latex-message-code 'utf-8)

(setq YaTeX-use-LaTeX2e t)
(setq YaTeX-use-AMS-LaTeX t)

;;(setq YaTeX-dvi2-command-ext-alist
;;    '(("dviout" . ".dvi")
;;      ("psv" . ".ps")
;;      ("TeXworks\\|SumatraPDF\\|evince\\|okular\\|firefox\\|chrome\\|AcroRd32\\|pdfopen" . ".pdf")))


;;Yatexを起動した時のみ，"\C >"でcomment-region
(add-hook 'yatex-mode-hook
	  '(lambda ()
	     (define-key reftex-mode-map (concat YaTeX-prefix ">") 'YaTeX-comment-region)
	     (define-key reftex-mode-map (concat YaTeX-prefix "<") 'YaTeX-uncomment-region)))

;;;;;;;;;;;;;;;;;;;;;;;;;;
;; yatex setting file   ;;
;;;;;;;;;;;;;;;;;;;;;;;;;;
;;yatexの設定ファイルは，elispで書かれているので自分で色々カスタマイズすることができる．
;;先回りusepackage：：yatexpkg.elに設定がある．特にカスタムする場合はYaTeX-package-alist-privateを編集する．

;;;;;;;;;;;;;;;;;;;;;;;;;
;; yatexでoutline-modeを使う
;;;;;;;;;;;;;;;;;;;;;;;;;;
;;2020/4/7
;;http://www.math.s.chiba-u.ac.jp/~matsu/emacs/emacs21/outline.html
;;http://www.math.kobe-u.ac.jp/HOME/kodama/tips-latex-outline.html
;;outline自体の使い方は以下参照．prefixは\C^c @  代表的なコマンドは
;;prefix \C-c 隠す
;;prefix \C-e 表示する
;;prefix \C-n 次のところへ
;;prefix \C-p 前のところへ

;;https://ayatakesi.github.io/emacs/24.5/Outline-Mode.html#Outline-Mode

;; (defun latex-outline-level ()
;;   (interactive)
;;   (let ((str nil))
;; 	(looking-at outline-regexp)
;; 	(setq str (buffer-substring-no-properties (match-beginning 0) (match-end 0)))
;; 	(cond ;; キーワード に 階層 を返す
;; 	 ((string-match "documentclass" str) 1)
;; 	 ((string-match "documentstyle" str) 1)
;; 	 ((string-match "part" str) 2)
;; 	 ((string-match "chapter" str) 3)
;; 	 ((string-match "appendix" str) 3)
;; 	 ((string-match "subsubsection" str) 6)
;; 	 ((string-match "subsection" str) 5)
;; 	 ((string-match "section" str) 4)
;; 	 (t (+ 6 (length str)))
;; 	 )))

;; (add-hook 'yatex-mode-hook
;; 		  '(lambda ()
;; 			 (setq outline-level 'latex-outline-level)
;; 			 (make-local-variable 'outline-regexp)
;; 			 (setq outline-regexp
;; 				  (concat "[ \t]*\\\\\\(documentstyle\\|documentclass\\|"
;; 				          "part\\|chapter\\|appendix\\|section\\|subsection\\|subsubsection\\)"
;; 				          "\\*?[ \t]*[[{]"))
;; 			 (outline-minor-mode t)))
;; (setq outline-minor-mode-prefix "\C-c\C-o")

(add-hook 'yatex-mode-hook
          '(lambda () (outline-minor-mode t)))
;; prefixの変更
;; https://rion778.hatenablog.com/entry/20100214/1266151330
(add-hook 'outline-minor-mode-hook
	  (lambda () (local-set-key "\C-c\C-o"
				    outline-mode-prefix-map)))

(make-variable-buffer-local 'outline-regexp)
(add-hook
 'yatex-mode-hook
 (function
  (lambda ()
    (progn
      (setq outline-level 'latex-outline-level)
      (setq outline-regexp
            (concat "[ \t]*\\\\\\(documentstyle\\|documentclass\\|"
                    "chapter\\|section\\|subsection\\|subsubsection\\)"
                    "\\*?[ \t]*[[{]")
     )))))

(make-variable-buffer-local 'outline-level)
(setq-default outline-level 'outline-level)
(defun latex-outline-level ()
  (save-excursion
    (looking-at outline-regexp)
    (let ((title (buffer-substring (match-beginning 1) (match-end 1))))
      (cond ((equal (substring title 0 4) "docu") 15)
            ((equal (substring title 0 4) "chap") 0)
            ((equal (substring title 0 4) "appe") 0)
            (t (length title))))))

;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Tex->dvi （compile） ;;
;;;;;;;;;;;;;;;;;;;;;;;;;;
;;compileは\C-t-jで良い．

;;2019/11/13 latexmkの設定は~/.latexmkrcへどうぞ
;;2019/11/13 今まではC-c-t-jコマンドでptex2pdfを用いていたが，これからはlatexmkを使う．
;;というのも，bibtexを使いたくなったからで，latexmkならば面倒臭いbibtex関連のコンパイルをコマンド一つで実行できる．
;;https://qiita.com/Rumisbern/items/d9de41823aa46d5f05a8
(setq tex-command "latexmk")



;;;;=====================
;; dvi->pdf and Preview
;;;;=====================
;;
;;previewとしてskimを用いる．
;;skimのインストールが必要なので注意すること．
;;また，自動更新のためにはskimの環境設定->同期から少し弄る必要あり
(setq dvi2-command "open -a Skim")
;;
;;dviprintコマンド
;;https://www-he.scphys.kyoto-u.ac.jp/member/shotakaha/dokuwiki/doku.php?id=toolbox:emacs:yatex:start
(setq dviprint-command-format "dvipdfmx %s")
;;(setq dviprint-command-format "~/.emacs.d/dvpd.sh %s")
;;

;プレビュー時自動で拡張子を補完する
(defvar YaTeX-dvi2-command-ext-alist
  '(("[agx]dvi\\|dviout\\|emacsclient" . ".dvi")
    ("ghostview\\|gv" . ".ps")
    ("acroread\\|pdf\\|Preview\\|TeXShop\\|Skim\\|evince\\|apvlv" . ".pdf")))


;;bibtexコマンド
(setq bibtex-command (cond ((string-match "uplatex\\|-u" tex-command) "upbibtex")
			   ((string-match "platex" tex-command) "pbibtex -kanji=utf8")
			   ((string-match "lualatex\\|luajitlatex\\|xelatex" tex-command) "bibtexu")
			   ((string-match "pdflatex\\|latex" tex-command) "bibtex")
			   (t "pbibtex -kanji=utf8")))

;;make-indexはどうも索引を作るのに必要なようだ
;;これを見ると，どうもtex-commandに応じて使うindexコマンドを変えているみたい．
 (setq makeindex-command (cond ((string-match "uplatex\\|-u" tex-command) "mendex -U")
 			      ((string-match "platex" tex-command) "mendex -U")
 			      ((string-match "lualatex\\|luajitlatex\\|xelatex" tex-command) "texindy")
 			      ((string-match "pdflatex\\|latex" tex-command) "makeindex")
 			      (t "mendex -U")))


;;bibtexファイルの場所指定
;;(setq reftex-default-bibliography '("/path/to/bibtex/file/"))




;;;;==============================
;;;;==============================
;; RefTeX with YaTeX;
;;;;==============================
;;;;==============================

;;2020/4/10 現在はRefTeXの機能は使わずに，yatexのデフォルトの\ref，\cite機能を使っている．

;;参照文献の番号を加えたりするときに便利
;;http://mtino1594.hatenablog.com/entry/2019/04/07/200000#use-package-の大まかな使い方
;(add-hook 'yatex-mode-hook 'turn-on-reftex)
(add-hook 'yatex-mode-hook
	  '(lambda ()
	     (reftex-mode 1)))



;;;;===============================
;; Emacsに自動で追加されたやつ他
;; Emacsは設定が更新されると，init.elの末尾に追加していく
;;;;===============================
;;
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(beacon-color "yellow")
 '(custom-safe-themes
   '("4639288d273cbd3dc880992e6032f9c817f17c4a91f00f3872009a099f5b3f84" default))
 '(dashboard-items
   '((recents . 15)
     (projects . 5)
     (bookmarks . 5)
     (agenda . 5)))
 '(dashboard-set-navigator t)
 '(flycheck-checker-error-threshold 1000)
 '(org-agenda-files nil)
 '(org-bullets-bullet-list '("" "" "" "" "" "" "" "" "" "") t)
 '(package-selected-packages
   '(doom-modeline-now-playing doom hide-mode-line vterm eglot ## outline-magic py-autopep8 volatile-highlights w3m mew fill-column-indicator magit org-bullets org-pomodoro org-beautify-theme doom-modeline company-lsp lsp-ui lsp-mode blgrep clmemo amx which-key package-utils dashboard open-junk-file company-math company git-gutter+ git-gutter google-this selected symbol-overlay beacon anzu flycheck-color-mode-line ov rainbow-delimiters yatex spaceline-all-the-icons highlight-indentation indent-guide nyan-mode spaceline powerline total-lines helm imenu-list eyebrowse use-package gtags atom-one-dark-theme quickrun color-moccur yasnippet web-mode solarized-theme projectile neotree howm hiwin flycheck elscreen dumb-jump color-theme-sanityinc-solarized auto-complete all-the-icons)))

;;faceをいじる
;;https://qiita.com/AnchorBlues/items/91026c4f1c0745f5b851


