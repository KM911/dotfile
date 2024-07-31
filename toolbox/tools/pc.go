package tools

// pwd copy
// process work directory
import (
	"os"
	"os/exec"
	"path/filepath"

	"github.com/KM911/fish/fs"
)

func Copy(content string) {
	copy := exec.Cmd{
		Path: "/usr/bin/wl-copy",
		Args: []string{"/usr/bin/wl-copy", content},
	}
	copy.Run()
}

func Paste() string {
	r, w, _ := os.Pipe()
	paste := exec.Cmd{
		Path:   "/usr/bin/wl-paste",
		Stdout: w,
	}
	paste.Run()
	defer w.Close()
	buffer := make([]byte, 1024)
	n, err := r.Read(buffer)
	if err != nil {
		panic(err)
	}
	return string(buffer[:n])
}

func Pc() {
	// fs.WorkingDirectory
	if len(os.Args) > 1 {
		Copy(filepath.Join(fs.WorkingDirectory, os.Args[1]))
	} else {

		Copy(fs.WorkingDirectory)
	}
}
